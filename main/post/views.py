from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from rest_framework import generics, viewsets
from django.views.generic.base import View

from post.models import Post, Comments
from post.forms import FormComments
from post.serializers import AllPostSerializer, AllPostComments

"""Настроил редирект с главной"""


def redirect_view(request):
    response = redirect('/blog')
    return response


"""Вывод список постов"""


class BlogView(ListView):
    model = Post
    queryset = Post.objects.filter(post_draft=True).order_by('-post_date')
    template_name = 'index.html'
    paginate_by = 9


"""Деталка поста"""


class BlogDetailView(DetailView):
    model = Post
    slug_field = 'post_slug'
    template_name = 'post.html'
    context_object_name = 'post'


"""Категории поста"""


class BlogCategory(ListView):
    model = Post
    slug_field = 'category_slug'
    template_name = 'index.html'
    paginate_by = 9

    def get_queryset(self):
        return Post.objects.filter(post_category__category_slug=self.kwargs['category_slug'], post_draft=True).order_by(
            '-post_date')


"""Представление сериалайзера постов"""


class AllBlogAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = AllPostSerializer
    lookup_field = "post_slug"
    lookup_url_kwarg = "post_slug"


"""Представление сериалайзера комментов"""


class AllCommentsAPIView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = AllPostComments


"""Комментрирование"""


class AddComment(View):
    def post(self, request, pk):
        form = FormComments(request.POST)
        comment_post = Post.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("comment_parent", None):
                form.parent_id = int(request.POST.get("comment_parent"))
            form.comment_post = comment_post
            form.save()
        return redirect(comment_post.get_absolute_url())


class Search(ListView):
    """Поиск по статьям"""
    paginate_by = 9
    template_name = 'index.html'

    def get_queryset(self):
        query = self.request.GET.get('query').capitalize()
        return Post.objects.filter(post_title__icontains=query)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = f'query={self.request.GET.get("query")}&'
        return context

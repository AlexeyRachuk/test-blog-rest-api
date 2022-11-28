from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from rest_framework import generics, viewsets

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


"""Возможность оставить комментарий"""


def post_comment(self):
    comments = Comments.comment_post.comment
    new_comment = None
    if self.method == 'POST':
        form = FormComments(self.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = Comments.comment_post
            new_comment.save()
    else:
        form = FormComments()
    return render(self, 'post.html', {'comments': comments, 'new_comment': new_comment, 'form': form})


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

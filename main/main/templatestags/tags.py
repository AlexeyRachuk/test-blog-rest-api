from django import template

from post.models import Category, Post

register = template.Library()


@register.inclusion_tag('tags/category.html')
def get_categories():
    categories = Category.objects.all()
    return {'category_all': categories}


@register.inclusion_tag('tags/last_blog.html')
def get_last_blog():
    last_blog = Post.objects.all().filter(post_draft=True).order_by('-post_date')[0:3]
    return {'last_blog_all': last_blog}

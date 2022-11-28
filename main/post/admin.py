from django.contrib import admin

from post.models import Post, Category, Comments

"""Админка постов"""


@admin.register(Post)
class PostAdminForm(admin.ModelAdmin):
    list_display = ('post_title', 'post_category', 'post_date', 'post_draft')
    list_filter = ('post_category',)
    search_fields = ('post_title',)
    list_editable = ('post_draft',)
    prepopulated_fields = {'post_slug': ('post_title',)}


"""Админка категорий"""


@admin.register(Category)
class CategoryAdminForm(admin.ModelAdmin):
    list_display = ('category_title',)
    prepopulated_fields = {'category_slug': ('category_title',)}

    """Админка комментариев (для самопроверки)"""


@admin.register(Comments)
class CommentsAdminForm(admin.ModelAdmin):
    list_display = ('comment_name',)

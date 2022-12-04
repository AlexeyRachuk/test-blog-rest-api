from datetime import date
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Модель категорий"""
    category_title = models.CharField('Название категории', max_length=80)
    category_slug = models.SlugField('URL категории', unique=True)

    def __str__(self):
        return self.category_title

    def get_absolute_url(self):
        return reverse('post_category', kwargs={'category_slug': self.category_slug})

    class Meta:
        verbose_name = "Категории статьи"
        verbose_name_plural = "Категории статьи"


class Post(models.Model):
    """Модель постов"""
    seo_title = models.CharField('SEO Title', max_length=70)
    seo_description = models.CharField('SEO Description', max_length=140)
    post_title = models.CharField('Заголовок статьи', max_length=100)
    post_slug = models.SlugField('URL cтатьи', unique=True)
    post_draft = models.BooleanField('Публикация новости', default=True)
    post_thumb_image = models.ImageField('Изобржение превью', upload_to='images/')
    post_thumb_text = models.TextField('Текст превью')
    post_category = models.ForeignKey(Category, verbose_name='Категория статьи', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField('Дата статьи', default=date.today)
    post_file = models.FileField('Видео или изображение статьи', upload_to='images/', null=True, blank=True)
    post_text = models.TextField('Содержимое статьи')

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.post_slug})

    class Meta:
        verbose_name = "Статьи"
        verbose_name_plural = "Статьи"


class Comments(models.Model):
    """Модель комментариев"""
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост',
                                     null=True, blank=True)
    comment_name = models.CharField('Имя', max_length=100)
    comment_text = models.TextField('Текст')
    comment_date = models.DateField(default=date.today)
    comment_parent = models.ForeignKey('self', verbose_name='Коментарий для ответа', on_delete=models.SET_NULL,
                                       blank=True, null=True, related_name='child')

    def __str__(self):
        return self.comment_name

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий"

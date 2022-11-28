from rest_framework import serializers

from post.models import Post, Comments


class AllPostSerializer(serializers.ModelSerializer):
    """Вывод всех постов в возможностью добавления. Здесь специально вывел просто все поля"""
    class Meta:
        model = Post
        fields = '__all__'


class AllPostComments(serializers.ModelSerializer):
    """Вывод всех комментариев"""
    class Meta:
        model = Comments
        fields = '__all__'

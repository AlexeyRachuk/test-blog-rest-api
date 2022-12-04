from rest_framework import serializers
import datetime

from post.models import Post, Comments, Category


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""

    def to_representation(self, data):
        data = data.filter(comment_parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вложенность комментариев"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class AllPostComments(serializers.ModelSerializer):
    """Вывод всех комментариев."""

    class Meta:
        model = Comments
        fields = '__all__'


class PostComments(serializers.ModelSerializer):
    child = RecursiveSerializer(many=True)
    """Вывод комментов поста, для удобства и описания вложенности"""

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Comments
        fields = ['comment_name', 'comment_text', 'comment_date', 'child']


class AllPostSerializer(serializers.ModelSerializer):
    post_category = serializers.SlugRelatedField(slug_field='category_title', queryset=Category.objects.all())
    comments = PostComments(many=True)
    """Вывод всех постов в возможностью добавления. Здесь специально вывел просто все поля и категорию назвнием. Привязал комментарии."""

    class Meta:
        model = Post
        fields = '__all__'

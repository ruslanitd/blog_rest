from rest_framework import serializers

from blog.models import Comment, Article


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('comment_article', 'comment_text', 'comment_date')


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'



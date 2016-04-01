from django.db import models


class Article(models.Model):
    article_name = models.CharField(max_length=100)
    article_text = models.TextField()
    article_date = models.TimeField(auto_now=True)

    def __str__(self):
        return self.article_name


class Comment(models.Model):
    comment_article = models.ForeignKey(Article, related_name='comments')
    comment_text = models.TextField()
    comment_date = models.TimeField(auto_now=True)

    def __str__(self):
        return self.comment_text

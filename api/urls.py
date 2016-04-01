from django.conf.urls import patterns, url


urlpatterns = patterns(
        'api.views',
        url(r'^blog/$', 'articles_list', name='articles_list'),
        url(r'^blog/(?P<pk>[0-9]+)$', 'article_detail', name='article_detail'),
        url(r'^blog/comments/(?P<article_pk>[0-9]+)$', 'comments_list', name='comments_list'),

)

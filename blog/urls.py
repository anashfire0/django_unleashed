from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.PostList.as_view(template_name='blog/post_list.html'),
            {'parent_template': 'base.html'}, name='blog_post_list'),
    re_path(r'^create/$', views.PostCreate.as_view(), name='blog_post_create'),
    re_path(r'^(?P<year>\d{4})/'
            r'(?P<month>\d{1,2})/'
            r'(?P<slug>[\w\-]+)/$',
            views.post_detail, {'parent_template': 'base.html'}, name='blog_post_detail'),
    re_path(r'^(?P<year>\d{4})/'
            r'(?P<month>\d{1,2})/'
            r'(?P<slug>[\w\-]+)/'
            r'update/$',
            views.PostUpdate.as_view(), name='blog_post_update'),
    re_path(r'^(?P<year>\d{4})/'
            r'(?P<month>\d{1,2})/'
            r'(?P<slug>[\w\-]+)/'
            r'delete/$',views.PostDelete.as_view(), name='blog_post_delete'),
    re_path(r'^(?P<year>\d{4})$/'
            r'delete/$',views.PostArchiveYear.as_view(), name='blog_archive_year'),
]

from django.urls import re_path, path
from . import views
from django.http import HttpResponse

urlpatterns = [
    re_path(r'^tag/$', views.TagList.as_view(), name='organizer_tag_list'),
    re_path(r'^tag/(?P<page_number>\d+)/$', views.TagPageList.as_view(), name='organizer_tag_page'),
    re_path(r'^tag/create/$', views.TagCreate.as_view(),
            name='organizer_tag_create'),
    re_path(r'^tag/(?P<slug>[\w\-]+)/$',
            views.tag_detail, name='organizer_tag_detail'),
    re_path(r'^tag/(?P<slug>[\w\-]+)/delete/$',
            views.TagDelete.as_view(), name='organizer_tag_delete'),
    re_path(r'^startup/$', views.StartUpList.as_view(), name='organizer_startup_list'),
    re_path(r'^startup/create/$', views.StartUpCreate.as_view(),
            name='organizer_startup_create'),
    re_path(r'^startup/(?P<slug>[\w\-]+)/$', views.StartUpDetail.as_view(), name='organizer_startup_detail'),
    re_path(r'^newslink/create$', views.NewsLinkCreate.as_view(),
            name='organizer_newslink_create'),
    re_path(r'^newslink/delete/(?P<pk>\d+)/$', views.NewsLinkDelete.as_view(),
            name='organizer_newslink_delete'),
    re_path(r'^newslink/update/(?P<pk>\d+)/$', views.NewsLinkUpdate.as_view(),
            name='organizer_newslink_update'),
    re_path(r'^tag/(?P<slug>[\w\-]+)/update/$',
            views.TagUpdate.as_view(), name='organizer_tag_update'),
    re_path(r'^startup/(?P<slug>[\w\-]+)/update/$',
            views.StartUpUpdate.as_view(), name='organizer_startup_update'),
    re_path(r'^startup/(?P<slug>[\w\-]+)/delete/$',
            views.StartUpDelete.as_view(), name='organizer_startup_delete')
]

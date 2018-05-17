from django.urls import re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView

app_name = 'user'

urlpatterns = [
    re_path(r'^login/$', auth_views.login,
            {'template_name': 'user/login.html'}, name='login'),
    re_path(r'^logout/$', auth_views.logout,
            {'template_name': 'user/logged_out.html', 'extra_context': {'form': AuthenticationForm}}, name='logout'),
    re_path(r'^$', RedirectView.as_view(
        pattern_name='user:login', permanent=False)),
]

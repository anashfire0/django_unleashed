"""pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include, reverse
from organizer import views
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.flatpages import urls as flatpages_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('organizer/', include('organizer.urls')),
    path('blog/', include('blog.urls')),
    path('', lambda request: HttpResponseRedirect(reverse('blog_post_list'))),
    # path('', lambda request: redirect('blog_post_list'))
    path('contact/', include('contact.urls')),
    re_path(r'^', include(flatpages_urls)),
    # path('', include(flatpages_urls)),
]

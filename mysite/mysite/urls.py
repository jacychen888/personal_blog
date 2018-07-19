"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from blog import views, search_views
from blog.feeds import BlogRssFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<blog_id>\d+)$', views.detail, name='blog_id'),
    url(r'^search/', search_views.MySearchView(), name='haystack_search'),
    url(r'^about/', views.about, name='about'),
    url(r'^archive/', views.archive, name='archive'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^rss/$', BlogRssFeed(), name='rss'),

]



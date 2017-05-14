from django.conf.urls import url

from . import views

appname = 'Blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.blog, name='blog'),
]

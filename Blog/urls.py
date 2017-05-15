from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

appname = 'Blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/$', auth_views.login, name="signin"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
    url(r'^create/$', views.create, name="create"),
    url(r'^(?P<year>[0-9]+)/$', views.year, name='year'),
    url(r'^(?P<year>[0-9]+)/(?P<month>\w+)/$', views.month, name='month'),
    url(r'^(?P<year>[0-9]+)/(?P<month>\w+)/(?P<post_id>[0-9]+)/$', views.blog, name='blog'),
    url(r'^(?P<un>\w+)/', views.user, name='user')
]

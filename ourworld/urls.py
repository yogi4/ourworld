from django.conf.urls import patterns, include,url
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from django.contrib.auth.models import AbstractUser
from letsdoit.api import CategoryDetail


admin.autodiscover()

class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='followers', symmetrical=False)

class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
"""
services_urls = patterns('',
                       #  url(r'^services/$',CategoryDetail.as_view(), name='service-list'),
                         url(r'^services/$',CategoryDetail.as_view()),
                         )
"""
urlpatterns = patterns('',

    #(r'^letsdoit/$', 'letsdoit.views.index'),
    #(r'^letsdoit/(?P<poll_id>\d+)/$', 'letsdoit.views.detail'),
    #(r'^letsdoit/(?P<poll_id>\d+)/results/$', 'letsdoit.views.results'),
    #(r'^letsdoit/(?P<poll_id>\d+)/vote/$', 'letsdoit.views.vote'),
    (r'^admin/', include(admin.site.urls)),

   #  url(r'^', include(router.urls)),
    # url(r'^$', CategoryDetail.as_view(), name='post-list'),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^services',CategoryDetail.as_view(),name='category-list'),

)


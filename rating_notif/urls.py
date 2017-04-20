from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^like_post/$', views.like_post),
    url(r'^unlike_post/$', views.unlike_post),
]

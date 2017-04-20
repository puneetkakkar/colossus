from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^add_new_user/$', views.add_new_user),
    url(r'^login_user/$', views.login_user),
    url(r'^logout/$', views.logout_user),
    url(r'^setting/$', views.change_password, name='change_password'),
]

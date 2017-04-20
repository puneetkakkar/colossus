from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^create_feed/$', views.create_feed),
	url(r'^add_follower/$', views.add_follower_to_user),
	url(r'^send_message/$', views.send_message),
	url(r'^profile_feed/(?P<requested_profile_link>[^/]+)/$', views.user_profile_feed),
	url(r'^(?P<requested_profile_link>[^/]+)/$', views.show_user_profile),
]

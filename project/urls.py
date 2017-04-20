from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$', views.add_project_page),
    url(r'^add_final/$', views.add_project),
    url(r'^project/$', views.add_project),
    url(r'^start/$', views.start_new),
    url(r'^view/$', views.view_project),
    url(r'^generate_stream_projects/$', views.generate_stream_projects),
    url(r'^view/(?P<requested_stream>[-\w]+)/$', views.view_project_stream),
    url(r'^(?P<requested_user>[-\w]+)/(?P<requested_profile_link>[^/]+)/$', views.show_project),
]

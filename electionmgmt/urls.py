from django.conf.urls import  url
from electionmgmt import views

urlpatterns = [
    url(r'^voters/$', views.voter_list),
    url(r'^voters/(?P<pk>[0-9]+)$', views.voter_detail),
]

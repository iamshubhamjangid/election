from django.conf.urls import url, include
from django.contrib import admin
from electionmgmt.views import VoterViewSet, CandidateViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'voters', VoterViewSet, base_name='voter')
router.register(r'candidates', CandidateViewSet, base_name='candidate')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^election', include('electionmgmt.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

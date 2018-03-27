# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from electionmgmt.models import Voter, Candidate
from electionmgmt.serializers import VoterSerializer, CandidateSerializer
from rest_framework.response import Response


class VoterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Voter.objects.all().order_by('name')
    serializer_class = VoterSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer



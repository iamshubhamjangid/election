# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from electionmgmt.models import Voter, Candidate
from electionmgmt.serializers import VoterSerializer, CandidateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def voter_list(request):
    if request.method == 'GET':
        voters = Voter.objects.all()
        voter_serializer = VoterSerializer(voters, many=True)
        return Response(voter_serializer.data)
    elif request.method == 'POST':
        voter_serializer = VoterSerializer(data=request.data)
        if voter_serializer.is_valid():
            voter_serializer.save()
            return Response(voter_serializer.data, status=status.HTTP_201_CREATED)
        return Response(voter_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def voter_detail(request, pk):
    try:
        voter = Voter.objects.get(pk=pk)
    except Voter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        voter_serializer = VoterSerializer(voter)
        return Response(voter_serializer.data)
    elif request.method == 'PUT':
        voter_serializer = VoterSerializer(voter, data= request.data)
        if voter_serializer.is_valid():
            voter_serializer.save()
            return Response(voter_serializer.data)
        return Response(voter_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        voter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import serializers
from electionmgmt.models import Voter, Candidate


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ('name', 'aadhar', 'vid', 'age')


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('name', 'aadhar', 'vid', 'cid', 'age')


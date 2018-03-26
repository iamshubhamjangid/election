from rest_framework import serializers
from electionmgmt.models import Voter, Candidate


class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ('name', 'aadhar', 'vid', 'age')

    def create(self, validated_data):
        return Voter.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.aadhar = validated_data.get('aadhar', instance.aadhar)
        instance.vid = validated_data.get('vid', instance.vid)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('name', 'aadhar', 'vid', 'cid', 'age')

    def create(self, validated_data):
        return Voter.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.aadhar = validated_data.get('aadhar', instance.aadhar)
        instance.vid = validated_data.get('vid', instance.vid)
        instance.cid = validated_data.get('cid', instance.cid)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance

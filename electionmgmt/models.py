# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models import signals


def add_voter(sender, instance, **kwargs):
    print "Voter is stored in the database!!"


def delete_voter(sender, instance, **kwargs):
    print "Voter Is deleted!!"


class Voter(models.Model):
    name = models.CharField(max_length=250)
    aadhar = models.CharField(max_length=100, unique=True)
    vid = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField()
    vtrevent = {name: vid}

    def __str__(self):
        return self.vid


signals.pre_save.connect(add_voter, sender=Voter)

signals.post_delete.connect(delete_voter, sender=Voter)


def add_candidate(sender, instance, **kwargs):
    print "Candidate is added to the store!!"


def delete_candidate(sender, instance, **kwargs):
    print "candidate is deleted !!"


class Candidate(models.Model):
    name = models.CharField(max_length=250)
    aadhar = models.CharField(max_length=100, unique=True)
    vid = models.ForeignKey(Voter)
    cid = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField()
    cdevent = {name: cid}

    def __str__(self):
        return self.name


signals.pre_save.connect(add_candidate, sender=Candidate)

signals.post_delete.connect(delete_candidate, sender=Candidate)


class Events(models.Model):
    event_type = models.CharField(max_length=100)
    # event_data =
    
    def __str__(self):
        return self.event_type

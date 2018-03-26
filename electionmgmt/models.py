# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Voter(models.Model):
    name = models.CharField(max_length=250)
    aadhar = models.CharField(max_length=100, unique=True)
    vid = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField()

    def __str__(self):
        return self.vid


class Candidate(models.Model):
    name = models.CharField(max_length=250)
    aadhar = models.CharField(max_length=100, unique=True)
    vid = models.ForeignKey(Voter)
    cid = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name

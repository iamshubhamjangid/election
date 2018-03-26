# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Voter, Candidate

admin.site.register(Voter)
admin.site.register(Candidate)
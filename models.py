# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models import signals
from kafka import KafkaProducer, KafkaConsumer


KAFKA_TOPIC = 'voters'
KAFKA_BROKERS = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKERS)
consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BROKERS,
                         auto_offset_reset='earliest')
msg = "ndjskbvks"


def add_voter(sender, instance, **kwargs):
    print "Voter is stored in the database!!"
    Events.objects.create(event_type="AddVoter", data=instance)
    # print(msg)
    producer.send('voters', value=b'Voter Is Added')


def delete_voter(sender, instance, **kwargs):
    print "Voter Is deleted!!"
    Events.objects.create(event_type="DeleteVoter", data=str(instance))
    producer.send('voters', value=b'Voter Is Deleted')


class Voter(models.Model):
    name = models.CharField(max_length=250)
    aadhar = models.CharField(max_length=100, unique=True)
    vid = models.CharField(max_length=100, primary_key=True)
    age = models.IntegerField()
    vtrevent = {name: vid}

    def __str__(self):
        return self.vid


signals.post_save.connect(add_voter, sender=Voter)

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
    data = models.CharField(max_length=200)

    def __str__(self):
        return self.event_type

from django.db import models
from django.contrib.models.Model

class Thing(Model):
    name = models.CharField()
    description = models.CharField()
    quanitity = models.IntegerField()

from django.db import models
#from django.contrib.models import Model

class Thing(models.Model):
    name = models.CharField(
        max_length = 50
    )
    description = models.CharField(
        max_length = 400
    )
    quanitity = models.IntegerField()

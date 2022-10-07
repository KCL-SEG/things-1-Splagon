from django.db import models
#from django.contrib.models import Model

class Thing(models.Model):
    name = models.CharField(
        max_length = 30
    )
    description = models.CharField(
        max_length = 400
    )
    quantity = models.IntegerField()

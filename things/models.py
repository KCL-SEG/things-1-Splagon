from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

class Thing(models.Model):
    name = models.CharField(
        max_length = 30,
        blank = False,
        unique = True
    )
    description = models.CharField(
        max_length = 120,
        blank = True,
        unique = False
    )
    quantity = models.IntegerField(
        unique = False,
        validators = [
            MinLengthValidator(0, message = "Quantity must be 0 or above"),
            MaxLengthValidator(100, message = "Quantity must be 100 or below")
        ]
    )

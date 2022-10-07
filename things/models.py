from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

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
        default = 0,
        validators = [
            MinValueValidator(0, message = "Quantity must be 0 or above"),
            MaxValueValidator(100, message = "Quantity must be 100 or below")
        ]
    )

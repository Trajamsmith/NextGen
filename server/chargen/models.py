from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Race(models.Model):
    name = models.CharField(max_length=30)
    ability_modifiers = ArrayField(
        ArrayField(
            models.IntegerField(default=0),
            size=5,
        )
    )

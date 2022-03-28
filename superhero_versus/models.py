from statistics import mode
from django.db import models


class Superhero(models.Model):
    # Superheros includes villains, we aren't here to judge

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=False, null=False)
    full_name = models.CharField(max_length=255, unique=False, null=False)
    intelligence = models.IntegerField(null=True)
    strength = models.IntegerField(null=True)
    speed = models.IntegerField(null=True)
    durability = models.IntegerField(null=True)
    power = models.IntegerField(null=True)
    combat = models.IntegerField(null=True)

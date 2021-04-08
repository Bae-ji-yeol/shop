from django.db import models
from django.db.models import Model


# Create your models here.

class GeeksModel(models.Model):
    geeks_field = models.BooleanField(default=False)
    name = models.CharField(max_length=100)

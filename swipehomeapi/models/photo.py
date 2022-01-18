from django.db import models
from .house import House

class Photo(models.Model):
    
    href = models.CharField(max_length=200)
    house = models.ForeignKey(House, on_delete=models.DO_NOTHING)
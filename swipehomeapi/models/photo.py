from django.db import models

from swipehomeapi.models.house import House

class Photo(models.Model):
    
    href = models.CharField(max_length=200)
    
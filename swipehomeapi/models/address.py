from django.db import models
from .house import House

class Address(models.Model):
    
    line = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state_code = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=5)
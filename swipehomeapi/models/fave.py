from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .appuser import AppUser
from .house import House

class Fave(models.Model):
    
    app_user = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)
    house = models.ForeignKey(House, null=True, on_delete=models.DO_NOTHING)
    property_id = models.CharField(null=True, max_length=25)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state_code = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=5)
    beds = models.IntegerField(validators=[MinValueValidator(0)])
    baths = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20000000)])
    photo = models.CharField(max_length=150)
    timestamp = models.IntegerField()
    
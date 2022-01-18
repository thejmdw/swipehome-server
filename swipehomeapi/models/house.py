from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .address import Address
from .user_type import UserType
from .app_user import AppUser

class House(models.Model):
    
    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING)
    photos = [
        {
            "href": models.CharField(max)
        }
    ]
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20000000)])
    beds = models.IntegerField(validators=[MinValueValidator(0)])
    baths_full = models.IntegerField(validators=[MinValueValidator(1)])
    userTypeId = models.ForeignKey(UserType, on_delete=models.DO_NOTHING)
    userId = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)
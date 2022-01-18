from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .address import Address
from .usertype import UserType
from .appuser import AppUser
# from .photo import Photo

class House(models.Model):
    
    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING)
    # photos = models.ForeignKey(Photo, on_delete=models.DO_NOTHING)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20000000)])
    beds = models.IntegerField(validators=[MinValueValidator(0)])
    baths_full = models.IntegerField(validators=[MinValueValidator(1)])
    userType = models.ForeignKey(UserType, on_delete=models.DO_NOTHING)
    app_user = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)
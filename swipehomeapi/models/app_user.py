from django.db import models
from django.contrib.auth.models import User


class AppUser(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatarURL = models.CharField(max_length=50)
    userTypeID = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
    firstTimeUser = models.BooleanField
from django.db import models
from django.contrib.auth.models import User
from .user_type import UserType


class AppUser(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatarURL = models.CharField(max_length=50)
    userTypeID = models.ForeignKey(UserType, on_delete=models.DO_NOTHING, related_name='types')
    firstTimeUser = models.BooleanField
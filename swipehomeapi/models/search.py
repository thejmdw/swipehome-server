from django.db import models
from .appuser import AppUser
from .usertype import UserType

class Search(models.Model):
    
    city = models.CharField(max_length=50)
    state_code = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=5)
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    userType = models.ForeignKey(UserType, on_delete=models.CASCADE)
    
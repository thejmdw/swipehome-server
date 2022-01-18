from django.db import models

class UserType(models.Model):
    type = models.CharField(max_length=6)

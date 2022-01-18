from django.db import models
from .appuser import AppUser

class Message(models.Model):
    
    userId = models.ForeignKey(AppUser, on_delete=models.DO_NOTHING)
    recipientId = models.IntegerField()
    text = models.CharField(max_length=500)
    timestamp = models.IntegerField()
    unread = models.BooleanField(default="true")
     
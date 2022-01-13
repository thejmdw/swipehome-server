from django.db import models

class Search(models.Model):
    
    city = models.CharField(max_length=50)
    state_code = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=5)
    userId = models.ForeignKey("User", on_delete=models.CASCADE)
    userTypeId = models.ForeignKey("UserType", on_delete=models.CASCADE)
    
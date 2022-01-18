from django.db import models

class HousePhoto(models.Model): 
    
    house = models.ForeignKey("House", on_delete=models.DO_NOTHING)
    photo = models.ForeignKey("Photo", on_delete=models.DO_NOTHING)
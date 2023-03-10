from django.db import models
from website.models import TurfManager
from versatileimagefield.fields import VersatileImageField

# Create your models here.

class Turf(models.Model):
    manager = models.ForeignKey(TurfManager, on_delete=models.CASCADE, null=True)
    turf_name = models.CharField(max_length=100)
    turf_place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    turf_image = models.ImageField( upload_to="image/testimagemodel/")
    
    def __str__(self):
        return str(self.turf_name)
    
class TimeSlot(models.Model):
    turf = models.ForeignKey(Turf,on_delete=models.CASCADE,null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=True)

    def __str__(self):
        return str(self.turf)
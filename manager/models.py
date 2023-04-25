from django.db import models
from website.models import TurfManager,TurfUser
from turfuser.models import BookDate
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
    manager = models.ForeignKey(TurfManager,on_delete=models.CASCADE,null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=True)
    status = models.IntegerField(default=0)
    turf_user = models.ForeignKey(TurfUser,on_delete=models.CASCADE,null=True)
    price = models.CharField(max_length=100)
    date_for_book = models.DateField()

    def __str__(self):
        return str(self.turf)
    
class Category(models.Model):
    turf = models.ForeignKey(Turf,on_delete=models.CASCADE,null=True)
    game = models.CharField(max_length=100)

    def __str__(self):
        return str(self.game)
    
class Event(models.Model):
    manager = models.ForeignKey(TurfManager,on_delete=models.CASCADE,null=True)
    turf = models.CharField(max_length=200)
    event_image = models.ImageField( upload_to="image/testimagemodel/")
    date = models.DateField()
    time = models.TimeField()
    game = models.CharField(max_length=100)
    event_title = models.CharField(max_length=200)
    entry_fee = models.CharField(max_length=100)
    strength = models.IntegerField()

    def __str__(self):
        return str(self.event_title)
    
class EventBook(models.Model):
    manager = models.ForeignKey(TurfManager,on_delete=models.CASCADE,null=True)
    event = models.ForeignKey(Event,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(TurfUser,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.user.name)
    

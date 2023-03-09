from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models
from versatileimagefield.fields import VersatileImageField


class User(AbstractUser):

    is_turfmanager = models.BooleanField("is turfmanager", default=False)
    is_user = models.BooleanField("is user", default=False)


class TurfManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="marketingmanager")

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    turf_place = models.TextField()
    district = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
    
class TurfUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return str(self.name)
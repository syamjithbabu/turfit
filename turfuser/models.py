from django.db import models
from website.models import TurfUser

# Create your models here.

class BookDate(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)
    
class Contact(models.Model):
    user_obj = models.ForeignKey(TurfUser,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    message = models.TextField()
    reply = models.CharField(max_length=2000,null=True)

    def __str__(self):
        return str(self.first_name)
from django.db import models

# Create your models here.

class BookDate(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)
    
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return str(self.first_name)
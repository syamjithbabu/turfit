from django.db import models

# Create your models here.

class BookDate(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)
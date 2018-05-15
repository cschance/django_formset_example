from django.db import models

# Create your models here.


class Car(models.Model):

    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    body_style = models.CharField(max_length=50)

from django.db import models

class Mobile(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

class Laptop(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

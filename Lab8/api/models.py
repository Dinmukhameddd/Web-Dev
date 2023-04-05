from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=300)
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



from django.db import models

# Create your models here.
class House(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.FloatField()
    address = models.CharField(max_length=80)
    image = models.ImageField()

    def __str__(self):
        return self.title
    

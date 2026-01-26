from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars")
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

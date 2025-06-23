from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=18)
    country = models.CharField(max_length=100, default='Mexico')
    city = models.CharField(max_length=100, default='Guadalajara')
    company = models.CharField(max_length=100, default='None')
    position = models.CharField(max_length=100, default='None')
    
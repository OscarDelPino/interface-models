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
    
    def __str__(self):
        return self.user.username
    
    def get_user_data(self):
        return {
            'username': self.user.username,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'email': self.user.email,
            'age': self.age,
            'country': self.country,
            'city': self.city,
            'company': self.company,
            'position': self.position
        }

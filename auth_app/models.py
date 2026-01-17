from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    
    USER_TYPE=[
        ('Admin', 'Admin'),
        ('User', 'User'),
    ]
    full_name=models.CharField(max_length=100, null=True)
    usertype=models.CharField(choices=USER_TYPE, max_length=100, null=True)
    
    def __str__(self):
        return self.full_name
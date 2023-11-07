from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=250)
    email = models.EmailField(max_length=250,unique=True)
    profile_image = models.ImageField()
    phone_number = models.IntegerField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



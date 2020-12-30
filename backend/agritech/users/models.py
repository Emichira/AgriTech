from django.contrib.auth import login
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from datetime import datetime

class User(AbstractUser):
    #Boolean fields to select the type of user account.
    is_buyer     = models.BooleanField(default=False)
    is_seller    = models.BooleanField(default=False)
    created_at   = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email

# user model for farmers selling farm produces
class Seller(models.Model):
    seller = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=200, null=True)
    location     = models.CharField(max_length=200, null=True)
    county       = models.CharField(max_length=200, null=True)
    country      = models.CharField(max_length=200, null=True)
    description  = models.TextField(null=True, blank=True)
    created_at   = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email

#user model for customers buying farm produces
class Buyer(models.Model):
    buyer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    created_at   = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email


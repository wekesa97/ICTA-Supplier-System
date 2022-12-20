from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

# class User(AbstractUser):
#     is_agent = models.BooleanField(default=False)

class Supplier(models.Model):
    name = models.CharField(max_length=20)
    score = models.IntegerField(null=True,blank=True)
    is_verified = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.name
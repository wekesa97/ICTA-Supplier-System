from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=20)
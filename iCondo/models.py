from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Common_Areas(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    description  = models.TextField(max_length= 120)

    def __str__(self):
        return f"{self.name}"

from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ci = models.IntegerField(max_length=8)
#    list_display = ("username", "first_name", "last_name", "ci", "email")
    pass

class Common_Areas(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    description  = models.TextField(max_length= 120)

    def __str__(self):
        return f"{self.name}"

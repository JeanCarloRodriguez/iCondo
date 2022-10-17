from django.contrib import admin
from .models import User

# Register your models here.
class UserModel(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "ci", "email")

admin.site.register(User, UserModel)

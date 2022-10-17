from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("commonArea", views.common_area, name="common_area"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
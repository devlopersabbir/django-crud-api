from django.urls import path
from . import controllers

urlpatterns = [
    path("users/", controllers.getUsers, name="get all user")
]
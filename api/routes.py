from django.urls import path
from . import controllers

urlpatterns = [
    path("api/v1/users/", controllers.getUsers, name="get all user")
]
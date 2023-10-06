from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def getUsers (request):
    data = {
        "name":"Sabbir Hossain",
        "email": "dev@dev.com",
        "password": "dev2020"
    }
    HttpResponse.status_code = 200
    return JsonResponse(data, safe=True)
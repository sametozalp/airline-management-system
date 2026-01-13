from django.shortcuts import render
from .models import Airplane
from django.http import JsonResponse

# Create your views here.

def get_all(req):
    airplanes = Airplane.objects.all()
    data = {
        'airplanes': list(airplanes.values())
    }
    return JsonResponse(data)
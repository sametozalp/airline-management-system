from django.shortcuts import render
from.models import Flight
from django.http import JsonResponse

# Create your views here.

def get_all(req):
    flights = Flight.objects.all()
    data = {
        'flights': list(flights.values())
    }

    return JsonResponse(data)
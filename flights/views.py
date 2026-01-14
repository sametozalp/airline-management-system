from django.shortcuts import render
from.models import Flight
from rest_framework.response import Response
from .serializers import FlightDetailSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def get_all(req):
    flights = Flight.objects.all()
    serializer = FlightDetailSerializer(flights, many=True)
    return Response(serializer.data)
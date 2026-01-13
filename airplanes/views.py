from django.shortcuts import render
from .models import Airplane
from rest_framework.response import Response
from .serializers import AirplaneSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def get_all(req):
    airplanes = Airplane.objects.all()
    serializer = AirplaneSerializer(airplanes, many=True)
    return Response(serializer.data)
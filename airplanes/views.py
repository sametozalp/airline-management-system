from django.shortcuts import render
from .models import Airplane
from rest_framework.response import Response
from .serializers import AirplaneBasicSerializer, AirplaneDetailSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def get_all(req):
    airplanes = Airplane.objects.all()
    serializer = AirplaneBasicSerializer(airplanes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_detail(req, id):
    airplane = Airplane.objects.get(id=id)
    serializer = AirplaneDetailSerializer(airplane)
    return Response(serializer.data)
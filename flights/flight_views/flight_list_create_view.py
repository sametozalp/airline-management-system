from django.shortcuts import render
from ..models import Flight
from rest_framework.response import Response
from ..serializers.flight_basic_serializer import  FlightBasicSerializer
from ..serializers.flight_create_serialize import FlightCreateSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class FlightListCreateView(APIView):
    
    def get(self, req):
        flights = Flight.objects.all()
        serializer = FlightBasicSerializer(flights, many=True)
        return Response(serializer.data)
    
    def post(self, req):
        serializer = FlightCreateSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        
from django.shortcuts import render
from .models import Flight
from rest_framework.response import Response
from .serializers.flight_basic_serializer import  FlightBasicSerializer
from .serializers.flight_detail_serializer import FlightDetailSerializer
from .serializers.flight_create_serialize import FlightCreateSerializer
from .serializers.flight_update_serialize import FlightUpdateSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.

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
        
class FlightUpdateDetailView(APIView):

    def get(self, req, id):
        flight = get_object_or_404(Flight, id=id)
        serializer = FlightDetailSerializer(flight)
        return Response(serializer.data)
    
    def put(self, req, id):
        flight = get_object_or_404(Flight, id=id)
        serializer = FlightUpdateSerializer(flight, data = req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, req, id):
        flight = get_object_or_404(Flight, id=id)
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

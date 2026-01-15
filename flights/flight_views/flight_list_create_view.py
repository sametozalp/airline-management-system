from django.shortcuts import render
from ..models import Flight
from rest_framework.response import Response
from ..serializers.flight_basic_serializer import  FlightBasicSerializer
from ..serializers.flight_create_serializer import FlightCreateSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

class FlightListCreateView(APIView):
    
    def get(self, req):
        flights = Flight.objects.all()
        serializer = FlightBasicSerializer(flights, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body=FlightCreateSerializer
    )
    def post(self, req):
        serializer = FlightCreateSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
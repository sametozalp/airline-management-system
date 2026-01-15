from django.shortcuts import render
from ..models import Flight
from rest_framework.response import Response
from ..serializers.flight_basic_serializer import  FlightBasicSerializer
from ..serializers.flight_create_serializer import FlightCreateSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

class FlightListCreateView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['destination', 'departure', 'airplane', 'departure_time', 'arrival_time']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FlightCreateSerializer
        return FlightBasicSerializer
    
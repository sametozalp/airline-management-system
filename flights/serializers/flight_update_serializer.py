from rest_framework import serializers
from ..models import Flight
from .flight_create_update_base_serializer import FlightCreateUpdateBaseSerializer

class FlightUpdateSerializer(FlightCreateUpdateBaseSerializer):
    class Meta:
        model = Flight
        fields = "__all__"
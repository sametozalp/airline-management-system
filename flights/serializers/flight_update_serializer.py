from rest_framework import serializers
from ..models import Flight

class FlightUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["airplane", "arrival_time", "departure_time"]
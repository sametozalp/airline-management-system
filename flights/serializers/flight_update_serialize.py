from rest_framework import serializers
from ..models import Flight

class FlightUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["id", "airplane", "arrival_time"]
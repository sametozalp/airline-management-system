from .models import Flight
from rest_framework.serializers import ModelSerializer
from airplanes.serializers import AirplaneSerializer

class FlightSerializer(ModelSerializer):
    
    airplane = AirplaneSerializer()

    class Meta:
        model = Flight
        fields = "__all__"
from ..models import Flight
from rest_framework.serializers import ModelSerializer
from airplanes.serializers.airplane_basic_serializer import AirplaneBasicSerializer

class FlightBasicSerializer(ModelSerializer):
    
    airplane = AirplaneBasicSerializer()

    class Meta:
        model = Flight
        fields = ["id", "flight_number", "departure", "destination", "airplane"]
from .models import Flight
from rest_framework.serializers import ModelSerializer
from airplanes.serializers import AirplaneBasicSerializer

class FlightBasicSerializer(ModelSerializer):
    
    airplane = AirplaneBasicSerializer()

    class Meta:
        model = Flight
        fields = ["id", "flight_number", "departure", "destination"]

class FlightDetailSerializer(ModelSerializer):
    
    airplane = AirplaneBasicSerializer()

    class Meta:
        model = Flight
        fields = "__all__"
from ..models import Flight
from rest_framework.serializers import ModelSerializer
from airplanes.serializers.airplane_detail_serializer import AirplaneDetailSerializer

class FlightDetailSerializer(ModelSerializer):
    
    airplane = AirplaneDetailSerializer()

    class Meta:
        model = Flight
        fields = "__all__"
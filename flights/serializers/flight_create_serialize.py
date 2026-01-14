from rest_framework.serializers import ModelSerializer
from ..models import Flight

class FlightCreateSerializer(ModelSerializer):
    class Meta:
        model = Flight
        exclude = ["id"]
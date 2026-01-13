from .models import Flight
from rest_framework.serializers import ModelSerializer

class FlightSerializer(ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"
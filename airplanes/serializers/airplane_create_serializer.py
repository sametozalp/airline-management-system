from rest_framework import serializers
from ..models import Airplane
from .airplane_create_update_base_serializer import AirplaneCreateUpdateBaseSerializer

class AirplaneCreateSerializer(AirplaneCreateUpdateBaseSerializer):
    class Meta:
        model = Airplane
        exclude = ["status"]
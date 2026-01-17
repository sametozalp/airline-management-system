from rest_framework import serializers
from ..models import Airplane
from .airplane_create_update_base_serializer import AirplaneCreateUpdateBaseSerializer

class AirplaneUpdateSerializer(AirplaneCreateUpdateBaseSerializer):

    status = serializers.BooleanField(allow_null=False, required=True)

    class Meta:
        model = Airplane
        fields = ["tail_number", "model", "capacity", "production_year", "status"]
from rest_framework import serializers
from ..models import Airplane

class AirplaneUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ["tail_number", "model", "capacity", "production_year", "status"]
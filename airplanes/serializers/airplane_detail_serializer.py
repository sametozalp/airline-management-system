from rest_framework import serializers
from ..models import Airplane

class AirplaneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = "__all__"
from rest_framework import serializers
from .models import Airplane

class AirplaneBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ["id", "tail_number", "model", "capacity"]

class AirplaneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = "__all__"
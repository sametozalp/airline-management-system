from rest_framework.serializers import ModelSerializer
from ..models import Airplane

class AirplaneCreateSerializer(ModelSerializer):
    class Meta:
        model = Airplane
        exclude = ["status"]
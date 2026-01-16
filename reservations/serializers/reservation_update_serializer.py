from ..models import Reservation
from rest_framework.serializers import ModelSerializer

class ReservationUpdateSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["passenger_name", "passenger_email", "flight", "status"]
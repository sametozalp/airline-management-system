from rest_framework.serializers import ModelSerializer
from .models import Reservation

class ReservationDetailSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

class ReservationBasicSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["id", "passenger_name", "reservation_code", "flight"]
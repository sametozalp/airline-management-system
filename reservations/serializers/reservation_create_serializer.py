from rest_framework.serializers import ModelSerializer
from ..models import Reservation

class ReservationCreateSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        exclude = ["id", "created_at", "reservation_code"]
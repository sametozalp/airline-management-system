from rest_framework import serializers
from ..models import Reservation
from .reservation_create_update_base_serializer import ReservationCreateUpdateSerializer

class ReservationCreateSerializer(ReservationCreateUpdateSerializer):
    class Meta:
        model = Reservation
        exclude = ["created_at", "reservation_code", "status"]


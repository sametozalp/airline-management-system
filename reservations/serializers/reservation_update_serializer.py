from ..models import Reservation
from rest_framework import serializers
from .reservation_create_update_base_serializer import ReservationCreateUpdateSerializer

class ReservationUpdateSerializer(ReservationCreateUpdateSerializer):
    status = serializers.BooleanField(allow_null=False, required=True)

    class Meta:
        model = Reservation
        fields = ["passenger_name", "passenger_email", "flight", "status"]
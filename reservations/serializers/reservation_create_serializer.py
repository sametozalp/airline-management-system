from rest_framework import serializers
from ..models import Reservation

class ReservationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        exclude = ["created_at", "reservation_code", "status"]

    def validate(self, data):
        flight = data.get('flight')
        capacity = flight.airplane.capacity

        current_reservations = Reservation.objects.filter(flight=flight).count()

        if(current_reservations >= capacity):
            raise serializers.ValidationError("No capacity!")
        
        return data
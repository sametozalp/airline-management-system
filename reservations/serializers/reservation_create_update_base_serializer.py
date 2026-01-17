from rest_framework import serializers
from ..models import Reservation

class ReservationCreateUpdateSerializer(serializers.ModelSerializer):
    passenger_name = serializers.CharField(allow_null=False, allow_blank=False, required=True)
    passenger_email = serializers.EmailField(allow_null=False, required=True)

    def validate(self, data):
        flight = data.get('flight')
        capacity = flight.airplane.capacity

        current_reservations = Reservation.objects.filter(flight=flight)

        # if is it update, exclude me
        if self.instance:
            current_reservations = current_reservations.exclude(pk=self.instance.pk)

        if(current_reservations.count() >= capacity):
            raise serializers.ValidationError("No capacity!")
        
        return data
    
    def validate_passenger_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Your name can not be less 3 character")
        return value
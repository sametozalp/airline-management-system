from rest_framework import serializers
from datetime import timedelta
from ..models import Flight
from django.utils import timezone

class FlightCreateUpdateBaseSerializer(serializers.ModelSerializer):
    flight_number = serializers.CharField(allow_null=False, allow_blank=False, required=True)
    departure = serializers.CharField(allow_null=False, allow_blank=False, required=True)
    destination = serializers.CharField(allow_null=False, allow_blank=False, required=True)
    arrival_time = serializers.DateTimeField(allow_null=False, required=True)
    departure_time = serializers.DateTimeField(allow_null=False, required=True)
    
    def validate(self, data):
        airplane = data.get('airplane')
        departure_time = data.get('departure_time')
        arrival_time = data.get('arrival_time')

        if airplane == None or departure_time == None or arrival_time == None:
            serializers.ValidationError("Null value detected.")

        time_break = timedelta(hours=1)
        
        conflict_flights = Flight.objects.filter(
            airplane=airplane
        ).filter(
            departure_time__lt=arrival_time + time_break, # less than
            arrival_time__gt=departure_time - time_break # greater than
        )

        if conflict_flights.exists():
            raise serializers.ValidationError("The airplane is not available for this flight.")
        
        return data

    def validate_flight_number(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Flight number must greater than 3 character")
        return value
    
    def validate_departure_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("The departure time cannot be in the past")
        return value
    
    def validate_arrival_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("The arrival time cannot be in the past")
        return value
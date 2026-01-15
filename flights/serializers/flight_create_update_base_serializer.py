from rest_framework import serializers
from datetime import timedelta
from ..models import Flight

class FlightCreateUpdateBaseSerializer(serializers.ModelSerializer):
    
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

from rest_framework.serializers import ModelSerializer
from ..models import Reservation
from flights.serializers.flight_basic_serializer import FlightBasicSerializer

class ReservationBasicSerializer(ModelSerializer):

    flight = FlightBasicSerializer()

    class Meta:
        model = Reservation
        fields = ["id", "passenger_name", "reservation_code", "flight"]
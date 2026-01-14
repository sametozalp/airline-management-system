from rest_framework.serializers import ModelSerializer
from ..models import Reservation
from flights.serializers.flight_basic_serializer import FlightBasicSerializer

class ReservationDetailSerializer(ModelSerializer):

    flight = FlightBasicSerializer()

    class Meta:
        model = Reservation
        fields = "__all__"
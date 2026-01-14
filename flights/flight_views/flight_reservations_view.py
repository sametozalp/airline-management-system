from rest_framework.views import APIView
from reservations.models import Reservation
from reservations.serializers.reservation_basic_serializer import ReservationBasicSerializer
from rest_framework.response import Response

class FlightReservationsView(APIView):
    def get(self, req, id):
        reservations = Reservation.objects.filter(flight=id)
        serializer = ReservationBasicSerializer(reservations, many=True)
        return Response(serializer.data)
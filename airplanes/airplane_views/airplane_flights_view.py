from rest_framework.views import APIView
from flights.models import Flight
from flights.serializers.flight_basic_serializer import FlightBasicSerializer
from rest_framework.response import Response

class AirplaneFlightsView(APIView):
    def get(self, req, id):
        flights = Flight.objects.filter(airplane=id)
        serializer = FlightBasicSerializer(flights, many=flights)
        return Response(serializer.data)

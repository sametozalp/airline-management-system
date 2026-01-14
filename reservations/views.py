from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Reservation
from rest_framework.response import Response
from .serializers import ReservationBasicSerializer

# Create your views here.

@api_view(['GET'])
def get_all(req):
    reservations = Reservation.objects.all()
    serializer = ReservationBasicSerializer(reservations, many=True)
    return Response(serializer.data)

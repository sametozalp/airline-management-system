from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Reservation
from rest_framework.response import Response
from .serializers.reservation_basic_serializer import ReservationBasicSerializer
from .serializers.reservation_detail_serializer import ReservationDetailSerializer

# Create your views here.

@api_view(['GET'])
def get_all(req):
    reservations = Reservation.objects.all()
    serializer = ReservationBasicSerializer(reservations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_detail(req, id):
    airplane = Reservation.objects.get(id=id)
    serializer = ReservationDetailSerializer(airplane)
    return Response(serializer.data)
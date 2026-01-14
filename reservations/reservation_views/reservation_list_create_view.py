from django.shortcuts import render
from rest_framework.decorators import api_view
from ..models import Reservation
from rest_framework.response import Response
from ..serializers.reservation_basic_serializer import ReservationBasicSerializer
from ..serializers.reservation_create_serializer import ReservationCreateSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class ReservationListCreateView(APIView):
    
    def get(self, req):
        reservartions = Reservation.objects.all()
        serializer = ReservationBasicSerializer(reservartions, many=True)
        return Response(serializer.data)
    
    def post(self, req):
        serializer = ReservationCreateSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
from django.shortcuts import render
from rest_framework.decorators import api_view
from ..models import Reservation
from rest_framework.response import Response
from ..serializers.reservation_detail_serializer import ReservationDetailSerializer
from ..serializers.reservation_update_serializer import ReservationUpdateSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

class ReservationUpdateDetailView(APIView):

    def get(self, req, id):
        reservartion = get_object_or_404(Reservation, id=id)
        serializer = ReservationDetailSerializer(reservartion)
        return Response(serializer.data)

    @swagger_auto_schema(
    request_body=ReservationUpdateSerializer
    )
    def patch(self, req, id):
        reservartion = get_object_or_404(Reservation, id=id)
        serializer = ReservationUpdateSerializer(reservartion, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

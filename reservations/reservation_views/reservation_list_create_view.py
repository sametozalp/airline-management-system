from django.shortcuts import render
from rest_framework.decorators import api_view
from ..models import Reservation
from rest_framework.response import Response
from ..serializers.reservation_basic_serializer import ReservationBasicSerializer
from ..serializers.reservation_create_serializer import ReservationCreateSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
# from ..mail_service import MailService
from utils.mail_method import send_email

class ReservationListCreateView(APIView):
    
    def get(self, req):
        reservartions = Reservation.objects.all()
        serializer = ReservationBasicSerializer(reservartions, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body=ReservationCreateSerializer
    )
    def post(self, req):
        serializer = ReservationCreateSerializer(data=req.data)
        if serializer.is_valid():
            saved = serializer.save()
            # mail = MailService()
            # mail.send_mail(
            #     subject="Created Reservation",
            #     content= saved.get_reservation_status_message(),
            #     to_email=req.data.get("passenger_email")
            # )
            send_email(subject=f"Created Reservation - {saved.reservation_code}", message=saved.get_reservation_status_message(), to=req.data.get("passenger_email"))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from ..models import Airplane
from rest_framework.response import Response
from ..serializers.airplane_basic_serializer import AirplaneBasicSerializer
from ..serializers.airplane_create_serializer import AirplaneCreateSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

class AirplaneListCreateView(APIView):
    
    def get(self, req):
        airplanes = Airplane.objects.all()
        serializer = AirplaneBasicSerializer(airplanes, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        request_body=AirplaneCreateSerializer
    )
    def post(self, req):
        serializer = AirplaneCreateSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
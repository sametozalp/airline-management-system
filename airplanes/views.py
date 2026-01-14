from django.shortcuts import render
from .models import Airplane
from rest_framework.response import Response
from .serializers.airplane_basic_serializer import AirplaneBasicSerializer
from .serializers.airplane_detail_serializer import AirplaneDetailSerializer
from .serializers.airplane_create_serializer import AirplaneCreateSerializer
from .serializers.airplane_update_serializer import AirplaneUpdateSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.

class AirplaneListCreateView(APIView):
    
    def get(self, req):
        airplanes = Airplane.objects.all()
        serializer = AirplaneBasicSerializer(airplanes, many=True)
        return Response(serializer.data)
    
    def post(self, req):
        serializer = AirplaneCreateSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        
class AirplaneUpdateDetailView(APIView):

    def get(self, req, id):
        airplane = get_object_or_404(Airplane, id=id)
        serializer = AirplaneDetailSerializer(airplane)
        return Response(serializer.data)
    
    def put(self, req, id):
        airplane = get_object_or_404(Airplane, id=id)
        serializer = AirplaneUpdateSerializer(airplane, data = req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
from django.shortcuts import render
from ..models import Airplane
from rest_framework.response import Response
from ..serializers.airplane_basic_serializer import AirplaneBasicSerializer
from ..serializers.airplane_detail_serializer import AirplaneDetailSerializer
from ..serializers.airplane_create_serializer import AirplaneCreateSerializer
from ..serializers.airplane_update_serializer import AirplaneUpdateSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class AirplaneUpdateDetailView(APIView):

    def get(self, req, id):
        airplane = get_object_or_404(Airplane, id=id)
        serializer = AirplaneDetailSerializer(airplane)
        return Response(serializer.data)
    
    def patch(self, req, id):
        airplane = get_object_or_404(Airplane, id=id)
        serializer = AirplaneUpdateSerializer(airplane, data = req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, req, id):
        airplane = get_object_or_404(Airplane, id=id)
        airplane.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

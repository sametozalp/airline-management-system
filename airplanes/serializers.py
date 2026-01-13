from rest_framework import serializers

class AirplaneSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tail_number = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=200)
    capacity = serializers.IntegerField()
    production_year = serializers.IntegerField()
    status = serializers.BooleanField()
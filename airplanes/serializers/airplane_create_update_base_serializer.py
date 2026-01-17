from rest_framework import serializers

class AirplaneCreateUpdateBaseSerializer(serializers.ModelSerializer):
    def validate_tail_number(self, value):
        if 3 < len(value) < 7:
            raise serializers.ValidationError("Tail number can not be less than 3 characters and more than 7 characters")
        return value
    
    def validate_production_year(self, value):
        if 1995 > value:
            raise serializers.ValidationError("Production year must greater than 1995") 
        return value
    
    def validate_capacity(self, value):
        if value > 0:
            raise serializers.ValidationError("Capacity must be greater than 0")
        return value
    
    def validate_model(self, value):
        if value is None or value == "":
            raise serializers.ValidationError("Model can not be blank")
        return value
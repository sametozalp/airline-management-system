from rest_framework import serializers

class AirplaneCreateUpdateBaseSerializer(serializers.ModelSerializer):
    tail_number = serializers.CharField(allow_null=False, allow_blank=False, required=True)
    model = serializers.CharField(allow_null=False, allow_blank=False, required=True)
    capacity = serializers.IntegerField(allow_null=False, required=True)
    production_year = serializers.IntegerField(allow_null=False, required=True)

    def validate_tail_number(self, value):
        print("tail number: " + str(value))
        if not 3 < len(value) < 7:
            print("girdi")
            raise serializers.ValidationError("Tail number can not be less than 3 characters and greater than 7 characters")
        print("girmedi")
        return value
    
    def validate_production_year(self, value):
        if 1995 > value:
            raise serializers.ValidationError("Production year must greater than 1995") 
        return value
    
    def validate_capacity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Capacity must be greater than 0")
        return value
    
    def validate_model(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Model can not be less than 3 characters")
        return value
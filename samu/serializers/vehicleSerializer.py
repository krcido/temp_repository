from rest_framework.serializers import ModelSerializer
from samu.models.vehicleModel import VehicleModels

class VehicleSerializer(ModelSerializer):
    class Meta:
        model = VehicleModels
        fields = '__all__'
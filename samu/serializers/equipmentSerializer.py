from rest_framework.serializers import ModelSerializer
from samu.models.equipmentModel import EquipmentModel

class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = EquipmentModel
        fields = '__all__'
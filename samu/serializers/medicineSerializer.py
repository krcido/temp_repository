from rest_framework.serializers import ModelSerializer
from samu.models.medicineModel import MedicineModel

class MedicineSerializer(ModelSerializer):
    class Meta:
        model = MedicineModel
        fields = '__all__'
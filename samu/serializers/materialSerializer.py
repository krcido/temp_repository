from rest_framework.serializers import ModelSerializer
from samu.models.materialModel import MaterialModel

class MaterialSerializer(ModelSerializer):
    class Meta:
        model = MaterialModel
        fields = '__all__'
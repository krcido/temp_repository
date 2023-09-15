from rest_framework.serializers import ModelSerializer
from samu.models.outputModel import OutPutModel

class OutPutSerializer(ModelSerializer):
    class Meta:
        model = OutPutModel
        fields = '__all__'
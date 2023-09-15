from rest_framework.serializers import ModelSerializer
from samu.models.statusRequestModel import StatusRequestModel

class StatusRequestSerializer(ModelSerializer):
    class Meta:
        model = StatusRequestModel
        fields = '__all__'
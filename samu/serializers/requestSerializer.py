from rest_framework.serializers import ModelSerializer
from samu.models.requestModel import RequestModel

class RequestSerializer(ModelSerializer):
    class Meta:
        model = RequestModel
        fields = '__all__'
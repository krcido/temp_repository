from rest_framework.serializers import ModelSerializer
from samu.models.requestTypeModel import RequestTypemodel

class RequestTypeSerializer(ModelSerializer):
    class Meta:
        model = RequestTypemodel
        fields = '__all__'
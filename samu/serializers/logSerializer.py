from rest_framework.serializers import ModelSerializer
from samu.models.logModel import LogModel

class LogSerializer(ModelSerializer):
    class Meta:
        model = LogModel
        fields = '__all__'
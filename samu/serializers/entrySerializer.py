from rest_framework.serializers import ModelSerializer
from samu.models.entryModel import EntrytModel

class EntrySerializer(ModelSerializer):
    class Meta:
        model = EntrytModel
        fields = '__all__'
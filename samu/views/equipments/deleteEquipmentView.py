from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from samu.models.equipmentModel import EquipmentModel
from samu.serializers.equipmentSerializer import EquipmentSerializer
from django.shortcuts import get_object_or_404

class DeleteEquipmentView(viewsets.ViewSet):
    #permission_classes = [IsAdminUser]

    def destroy(self, request, pk=None):
        equipment = get_object_or_404(EquipmentModel, pk=pk)
        try:
            equipment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

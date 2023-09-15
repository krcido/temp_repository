from rest_framework import viewsets, status
from samu.models.equipmentModel import EquipmentModel
from samu.serializers.equipmentSerializer import EquipmentSerializer
from rest_framework.response import Response

class GetEquipmentView(viewsets.ModelViewSet):
    #permission_classes = [IsSuperuserOrReadOnly]

    def retrieve(self, request, pk=None):
        try:
            equipment = EquipmentModel.objects.get(pk=pk)
            serializer = EquipmentSerializer(equipment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except EquipmentModel.DoesNotExist:
            return Response({"detail": "Equipamento não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

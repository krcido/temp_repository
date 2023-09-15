from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from samu.models.equipmentModel import EquipmentModel
from samu.serializers.equipmentSerializer import EquipmentSerializer

class UpdateEquipmentView(viewsets.ModelViewSet):
    #permission_classes = [IsSuperuserOrReadOnly]
    
    queryset = EquipmentModel.objects.all()
    serializer_class = EquipmentSerializer

    def update(self, request, *args, **kwargs):
        try:
            equipment = self.get_object()
            serializer = self.get_serializer(equipment, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except EquipmentModel.DoesNotExist:
            return Response({"detail": "O equipamento não foi encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": f"Ocorreu um erro: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


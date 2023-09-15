from rest_framework import viewsets, status
from samu.models.equipmentModel import EquipmentModel
from samu.serializers.equipmentSerializer import EquipmentSerializer
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse

class ListEquipementView(viewsets.ViewSet):
    # permission_classes = [IsSuperuserOrReadOnly]

    def list_equipement(self, request):
        try:

            equipamentos = EquipmentModel.objects.all()

            return render(request, 'lista_de_equipamentos.html', {'equipamentos': equipamentos})

        except Exception as e:
          
            return HttpResponse(f"Ocorreu um erro ao listar os equipamentos: {str(e)}", status=500)

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from samu.models.equipmentModel import EquipmentModel
from samu.serializers.equipmentSerializer import EquipmentSerializer
from django.shortcuts import redirect

class AddEquipmentView(viewsets.ViewSet):
    #permission_classes = [IsSuperuserOrReadOnly]

    def create_equipment(self, request, *arg, **kwargs):
        try:
            # Serializa os dados enviados na solicitação
            serializer = EquipmentSerializer(data=request.data)

            # Verifica se os dados são válidos
            if serializer.is_valid():
                # Cria um novo equipamento com base nos dados serializados
                serializer.save()

                # Redireciona para a URL desejada (modificar a url)
                return redirect('nome_da_url')

            # Se os dados não forem válidos, retorna uma resposta de erro com os detalhes dos erros
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Lida com exceções aqui, por exemplo, registre o erro ou retorne uma resposta de erro personalizada
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.urls import path
from samu.views.equipments.addEquipmentView import AddEquipmentView
from samu.views.equipments.deleteEquipmentView import DeleteEquipmentView
from samu.views.equipments.getEquipmentView import GetEquipmentView
from samu.views.equipments.listEquipmentView import ListEquipementView
from samu.views.equipments.updateEquipmentView import UpdateEquipmentView

urlpatterns = [
    path('list/', ListEquipementView.as_view({'get': 'list_equipement'}), name='list_equipment'),
    path('add/', AddEquipmentView.as_view({'post': 'create_equipment'}), name='add_equipment'),
    path('get/<int:pk>/', GetEquipmentView.as_view({'get': 'retrieve'}), name='get_equipment'),
    path('update/<int:pk>/', UpdateEquipmentView.as_view({'put': 'update'}), name='update_equipment'),
    path('delete/<int:pk>/', DeleteEquipmentView.as_view({'delete': 'delete_equipment'}), name='delete_equipment'),
]

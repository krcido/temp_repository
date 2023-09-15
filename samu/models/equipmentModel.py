from django.db import models
from samu.models.itemModel import ItemModel

class EquipmentModel(ItemModel):
    name = models.CharField(max_length=100)
    description  = models.CharField(max_length=300)
    patrimony  = models.CharField(max_length=45)
    allocable   = models.BooleanField()
    available  = models.BooleanField(default=True)
    warranty_expire  = models.DateField()
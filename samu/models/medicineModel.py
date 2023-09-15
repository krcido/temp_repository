from django.db import models
from samu.models.itemModel import ItemModel

class MedicineModel(ItemModel):
    name = models.CharField(max_length=100)
    measurement_unit  = models.IntegerField()
    presentation   = models.IntegerField()
    batch_code   = models.CharField(max_length=30)
    concentration = models.CharField(max_length=60)
    therapeutic_class = models.CharField(max_length=70)
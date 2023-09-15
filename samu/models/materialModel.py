from django.db import models
from samu.models.itemModel import ItemModel

class MaterialModel(ItemModel):
    id = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=300)
    batch_code = models.CharField(max_length=30, unique=True, null=False)
    allocable = models.BooleanField(null=False)
    expiration_date = models.DateField()
    


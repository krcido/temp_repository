from django.db import models
from samu.models.itemModel import ItemModel
from samu.models.vehicleModel import VehicleModels

class EntrytModel(models.Model):
    item_id = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField()
    available_quantity = models.IntegerField()
    vehicle_id = models.ForeignKey(VehicleModels, on_delete=models.CASCADE)
    reason = models.IntegerField()


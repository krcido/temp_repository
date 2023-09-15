from django.db import models

class VehicleModels(models.Model):
    available = models.BooleanField(default=True)
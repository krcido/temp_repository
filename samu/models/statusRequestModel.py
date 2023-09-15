from django.db import models

class StatusRequestModel(models.Model):
    name = models.CharField(max_length=50)
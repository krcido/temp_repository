from django.db import models
from samu.models.requestModel import RequestModel

class LogModel(models.Model):
    request_id = models.ForeignKey(RequestModel, on_delete=models.CASCADE)
    type = models.IntegerField(null=False)
    details = models.CharField(null=False)
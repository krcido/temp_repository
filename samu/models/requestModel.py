from django.db import models
from samu.models.userModel import UserModel
from samu.models.statusRequestModel import StatusRequestModel
from samu.models.requestTypeModel import RequestTypeModel

class RequestModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(StatusRequestModel, on_delete=models.CASCADE)
    type = models.ForeignKey(RequestTypeModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)

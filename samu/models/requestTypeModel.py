from django.db import models

class RequestTypeModel(models.Model):
     name = models.CharField(max_length=50)
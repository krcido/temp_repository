from django.db import models
from samu.models.entryModel import EntrytModel

class OutPutModel(models.Model):
    entry_id = models.ForeignKey(EntrytModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
    reason = models.IntegerField()

	
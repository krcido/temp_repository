from django.db import models

class ItemModel(models.Model):    
    type = models.BooleanField(default=True)

    class Meta:
        abstract = True  
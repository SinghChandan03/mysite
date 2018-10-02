from django.db import models
import django.utils.timezone
from datetime import datetime, timezone
from django.utils.timezone import now


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TemperatureCount(BaseModel):
    temp_value = models.FloatField(default=0)
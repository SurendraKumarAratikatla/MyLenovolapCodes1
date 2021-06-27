from django.db import models
from django.utils import timezone
import datetime

class Mobile(models.Model):
    brand = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.date, null=True, blank=True)

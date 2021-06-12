from django.db import models

class todo(models.Model):
    task = models.CharField(max_length=40)
    description = models.CharField(max_length=100)


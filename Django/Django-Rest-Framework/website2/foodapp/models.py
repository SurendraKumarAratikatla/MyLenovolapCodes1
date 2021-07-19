from django.db import models

class Laptop(models.Model):
    # OSTYPE = 'OS'
    # MODEL = 'MD'
    # RAM = 'RM'
    # HARDDISK = 'HD'
    CHARGER = 'CR'
    MOUSE = 'MU'

    FREE = [
        (CHARGER, 'Charger'),
        (MOUSE, 'Mouse'),
    ]

    des = ["Charger","Mouse"]
    name = models.CharField(max_length=100)
    free = models.CharField(max_length=2, choices= FREE, default= 'Charger')
    cost = models.IntegerField()
    #description = models.Field(max_length=200)

    def __str__(self):
        return self.name

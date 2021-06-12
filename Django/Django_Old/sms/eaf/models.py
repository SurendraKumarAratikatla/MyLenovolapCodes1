from django.db import models


class ChemicalElement(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Commodity(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500, default='DEFAULT VALUE')
    inventory = models.IntegerField(default=200)
    price = models.IntegerField(default=100)
    chemical_composition = models.IntegerField(default=15)
    def __str__(self):
        return self.name
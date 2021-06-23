from django.db import models

class Mobile(models.Model):
    brand = models.CharField(max_length=200)
    made_in = models.CharField(max_length=50)
    warranty = models.IntegerField()
    def __str__(self):
        return self.brand

class Laptop(models.Model):
    brand = models.CharField(max_length=200)
    made_in = models.CharField(max_length=50)
    warranty = models.IntegerField()
    def __str__(self):
        return self.brand

class TV(models.Model):
    brand = models.CharField(max_length=200)
    made_in = models.CharField(max_length=50)
    warranty = models.IntegerField()
    def __str__(self):
        return self.brand

class AC(models.Model):
    brand = models.CharField(max_length=200)
    made_in = models.CharField(max_length=50)
    warranty = models.IntegerField()
    def __str__(self):
        return self.brand


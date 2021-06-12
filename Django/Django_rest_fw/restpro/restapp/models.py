from django.db import models

class students(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

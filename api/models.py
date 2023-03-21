from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    cnic = models.IntegerField()
    contact = models.IntegerField()
    city = models.CharField(max_length=70)
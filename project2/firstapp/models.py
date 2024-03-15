from django.db import models

# Create your models here.

class Employee(models.Model):
      empId=models.IntegerField()
      name= models.CharField(max_length=15)
      course=models.CharField(max_length=10)
      location=models.CharField(max_length=10)

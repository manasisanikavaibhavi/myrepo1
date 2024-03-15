from django.db import models

# Create your models here.
class Student(models.Model):
   roll_Id=models.CharField(max_length=5)
   Name=models.CharField(max_length=15)
   Course=models.CharField(max_length=10)
   location=models.CharField(max_length=10)
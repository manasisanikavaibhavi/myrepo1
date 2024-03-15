from django.db import models
from.models import *



# Create your models here.
class Login(models.Model):
    email=models.CharField(max_length=25)
    password=models.CharField(max_length=20)

class Registration(models.Model):
     name=models.CharField(max_length=20)
     email=models.CharField(max_length=21)
     phone=models.CharField(max_length=11)
     address=models.CharField(max_length=20)
     country=models.CharField(max_length=12,default=True)
     city=models.CharField(max_length=10,default=True)
     region=models.CharField(max_length=11)
     code=models.CharField(max_length=12)
     

class feedback(models.Model):
     name=models.CharField(max_length=20)
     email=models.CharField(max_length=21)
     phone=models.CharField(max_length=12)
     satisfy=models.BooleanField()
     msg=models.CharField(max_length=30,default=True)   


class contact(models.Model):
     name=models.CharField(max_length=10)
     email=models.CharField(max_length=21)
     message=models.CharField(max_length=30)


class artistfrom(models.Model):
     name=models.CharField(max_length=10)
     art=models.CharField(max_length=12)
     artname=models.CharField(max_length=12)
     age=models.IntegerField()
     Amount=models.IntegerField()
     Nationality=models.CharField(max_length=12)
     email=models.CharField(max_length=12)
     phone=models.CharField(max_length=12)
     image=models.ImageField(upload_to="image")

class Payment(models.Model):
     name=models.CharField(max_length=10)
     cardname=models.CharField(max_length=12)
     email=models.CharField(max_length=12)
     address=models.CharField(max_length=20)
     city=models.CharField(max_length=10)
     pay_detail=models.CharField(max_length=16)
     cardno=models.CharField(max_length=20)
     cvc=models.CharField(max_length=12)
     month=models.CharField(max_length=10)
     year=models.CharField(max_length=10)
     amount=models.IntegerField()
     phoneno=models.CharField(max_length=10,default="8976543245")
     
     

     

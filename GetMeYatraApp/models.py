from django.db import models

# Create your models here.

class Book(models.Model):
    Place=models.CharField(max_length=100)
    Total_person= models.CharField(max_length=2)
    Adate=models.CharField(max_length=10)
    Ldate=models.CharField(max_length=10)
    Personaldata=models.TextField()
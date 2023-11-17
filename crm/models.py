from django.db import models

# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    salary=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    age=models.PositiveIntegerField(max_length=100)
    contact=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    dob=models.DateField(null=True,blank=True)





    

from django.db import models

# Create your models here.

#Creating database for the Employee

class Employee(models.Model):  
# Employee = Table Name 
# First_name,.... = Fields Name
    first_name= models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo= models.ImageField(upload_to='images')  
    designation=models.CharField(max_length=100)
    email_address= models.EmailField(max_length=100, unique=True)
    phone_number=models.CharField(max_length=12, blank=True)

# Blank = True makes a field Optional
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
from sre_constants import CATEGORY
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User

class Rcustomer(models.Model):
    user =models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    profile_pic =models.ImageField(default="profile1.jpg",null=True,blank=True)
    date_created =models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.user.username


class order(models.Model):
    STATUS1 =(
        ('pending' ,'pending'),
        ('Approved', 'Approved')
    )
    customer=models.ForeignKey(Rcustomer,null=True,on_delete=models.SET_NULL)
   # product=models.ForeignKey(product,null=True,on_delete=models.SET_NULL)
    status=models.CharField(max_length=200,null=True,choices=STATUS1)
    date_created =models.DateTimeField(auto_now_add=True,null=True)

class submit_order(models.Model):
    CATEGORY=(
        ('Appartment','Appartment'),
        ('Duplex','Duplex'),
        ('Villa','Villa'),
        ('Beach House','Beach House'),
        ('Commercial Space','Commercial Space'),
        ('Rental','Rental')
    )
    STATUS=(
        ('Approved','Approved'),
        ('Pending','Pending'),
        ('Failed','Failed')
    )
    name=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=50,null=True)
    property_type=models.CharField(max_length=100,null=False,choices=CATEGORY)
    length=models.CharField(max_length=200,null=False)
    breadth=models.CharField(max_length=100,null=False)
    Height=models.CharField(max_length=100,null=False)
    property_image =models.ImageField(null=True,blank=True)
    date_created =models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=100,null=True,choices=STATUS,default="Pending")
    delete_status=models.BooleanField(default=False)

    def __str__(self):
        return self.property_type

class contact_us(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=50,null=False)
    subject=models.CharField(max_length=100,null=False)
    message=models.CharField(max_length=500,null=False)

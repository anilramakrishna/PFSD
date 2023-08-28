
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','email','password1','password2','first_name']


class CustomerForm(ModelForm):
    class Meta:
        model=Rcustomer
        fields=['phone']
class CustomerForm1(ModelForm):
    class Meta:
        model=Rcustomer
        fields='__all__'
        exclude=['user']
class CustomerForm2(ModelForm):
    class Meta:
        model=User
        fields='__all__'

class CustomerSubmitPropertyForm(ModelForm):
    class Meta:
        model=submit_order
        fields=['name','property_type','email','length','breadth','Height','property_image']
        widgets = {
            'name': forms.TextInput(attrs={'disabled':True})
        }

        
class Update(ModelForm):
    class Meta:
        model=submit_order
        fields=['status']

class ContactForm(ModelForm):
    class Meta:
        model=contact_us
        fields='__all__'
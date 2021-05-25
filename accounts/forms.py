from django.forms import ModelForm, widgets, TextInput, Select
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models  import User
from .models import *

class OrderForm(ModelForm):

    class Meta :
        model = Order
        fields = '__all__'
       
class CustomerCreationForm(ModelForm):
    class Meta :
        model = Customer
        fields = '__all__'
       
class RegisterForm(UserCreationForm):

    class Meta :
        model = User
        fields = ['username','email','password1', 'password2']
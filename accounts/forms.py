from django.forms import ModelForm, widgets, TextInput, Select
from .models import *

class OrderForm(ModelForm):

    class Meta :
        model = Order
        fields = '__all__'
       
 
from django.forms import ModelForm, widgets, TextInput, Select
from .models import *

class OrderForm(ModelForm):

    class Meta :
        model = Order
        fields = '__all__'
       
class CustomerCreaionForm(ModelForm):
    class Meta :
        model = Customer
        fields = '__all__'
       
 
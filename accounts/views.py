from django.shortcuts import render
from .models import *

# home page
def index(response):
   
    return render(response, 'main/index.html')

# dashborad view
def dashboard(response):

    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = "Pending").count()

    context = {
        'orders' : orders,
        'customers' : customers,
        'total_orders':total_orders,
        'total_customers' :total_customers,
        'delivered' : delivered,
        'pending' : pending
    }
    return render(response, 'accounts/dashboard.html', context)

# products view 
def products(response):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(response, 'main/products.html', context)

# customer view 
def customer(response, pk):
    customer = Customer.objects.get(id =pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    context = {
        'customer' : customer,
        'orders' : orders,
        'total_orders' : total_orders
    }
    return render(response, 'accounts/customer.html', context )

def create_order(response):
    context = {}
    return render(response, 'accounts/order_form.html', context)

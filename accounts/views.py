from accounts.filters import OrderFilter
from django.http import request
from django.shortcuts import redirect, render
from django.forms import inlineformset_factory
from .models import *
from .forms import *
# from .filters import OrderFilter

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

    my_filter = OrderFilter()
    context = {
        'customer' : customer,
        'orders' : orders,
        'total_orders' : total_orders,
        'filter' : my_filter
    }
    return render(response, 'accounts/customer.html', context )

def create_order(response, pk):
    
    customer = Customer.objects.get(id = pk)
    form = OrderForm(initial={'customer': customer})
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra = 5)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)

    if response.method == "POST" :
        
        formset = OrderFormSet(response.POST, instance=customer)

        if formset.is_valid() :
            formset.save()

            return redirect('/customer/' + pk)

    context = {'formset':formset}
    return render(response, 'accounts/order_form.html', context)

def update_order(response, pk):
   
    
    order = Order.objects.get(id = pk)
    form = OrderForm(instance=order)
    context = {'form':form}

    if response.method == "POST" :
        form = OrderForm(response.POST, instance=order)
        if form.is_valid() :
            form.save()

            return redirect('/customer/' + str(order.customer.id))
    
    return render(response, 'accounts/update_form.html', context)

def delete_order (response, pk):
    order = Order.objects.get(id = pk)
    context = {'order' : order}

    if response.method == "POST" :
        
        order.delete()

        return redirect('/customer/' + str(order.customer.id))

    return render (response, 'accounts/delete.html',context )
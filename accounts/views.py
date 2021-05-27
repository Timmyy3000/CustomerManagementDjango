from django.contrib import auth
from accounts.filters import OrderFilter
from django.http import request
from django.shortcuts import redirect, render
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import * 
# from .filters import OrderFilter

# user page
def user_profile (response):

    return render(response,'accounts/profile.html')

#logout
def logoutUser(response):
    logout(response)
    return redirect('/')

# login in page
@unathenticated_user
def loginPage (response):
    context ={}

    if response.method == "POST":
        username = response.POST.get("username")
        password = response.POST.get("password")

        print(response.POST)

        user = authenticate(response, username = username , password = password)

        if user is not None :
            login(response, user)
            return redirect('dashboard')
        else :
            messages.error(response, "Username or Password is incorrect")
        
        
    return render(response, 'accounts/login.html', context)


# register 
@unathenticated_user
def register (response):
    form = RegisterForm()        

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid() :
            user = form.save()
            group = Group.objects.get(name = "Customer")
            user.groups.add(group)

            user_name = form.cleaned_data.get('username')
            messages.success(response, "Account Created Successfully for " + user_name)

            return redirect ('/login/')

    context ={'form' : form}

    return render(response, 'accounts/register.html', context)

# home page
def index(response):
   
    return render(response, 'main/index.html')

# dashborad view
@login_required(login_url='login')
@admin_only
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

# account setting view 
def account_settings(response):
    customer = response.user.customer
    form = CustomerUpdateForm(instance = customer)

    if response.method == "POST":

        form = CustomerUpdateForm(response.POST, response.FILES, instance=customer)

        if form.is_valid:
            form.save()
            messages.success(response, "Details updated successfully")
    
    context = {'form' : form}
    return render(response,'accounts/account_settings.html', context)
# products view 
def products(response):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(response, 'main/products.html', context)

# customer view 
@login_required(login_url='login')
def customer(response, pk):
    customer = Customer.objects.get(id =pk)
    orders = customer.order_set.all()
    total_orders = orders.count()

    my_filter = OrderFilter(response.GET, queryset=orders)
    orders= my_filter.qs

    context = {
        'customer' : customer,
        'orders' : orders,
        'total_orders' : total_orders,
        'filter' : my_filter
    }
    return render(response, 'accounts/customer.html', context )


# Create order view
@login_required(login_url='login')
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


# Update order view 
@login_required(login_url='login')
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

# delete order view
@login_required(login_url='login')
def delete_order (response, pk):

    order = Order.objects.get(id = pk)
    context = {'order' : order}

    if response.method == "POST" :
        
        order.delete()

        return redirect('/customer/' + str(order.customer.id))

    return render (response, 'accounts/delete.html',context )

# Create customer view 
@login_required(login_url='login')
def create_customer (response):

    form = CustomerCreationForm()
    
    
    if response.method == "POST" :
        
        form = CustomerCreationForm(response.POST)

        if form.is_valid() :
            form.save()
            return redirect('/dashboard/')
        
    context = {'form':form}

    return render(response, 'accounts/create_customer.html', context)

# Update customer view 
@login_required(login_url='login')
def update_customer(response, pk):
   
    
    customer = Customer.objects.get(id = pk)

    form = CustomerCreationForm(instance=customer)

    context = {'form':form}

    if response.method == "POST" :
        form = CustomerCreationForm(response.POST, instance=customer)
        if form.is_valid() :
            form.save()

            return redirect('/customer/' + str(customer.id))
    
    return render(response, 'accounts/update_form.html', context)

# delete customer view
@login_required(login_url='login')
def delete_customer (response, pk):

    customer = Customer.objects.get(id = pk)

    
    context = {'customer' : customer}

    if response.method == "POST" :
        
        customer.delete()

        return redirect('/dashboard/')

    return render (response, 'accounts/delete_customer.html',context )

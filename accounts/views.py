from django.shortcuts import render

# home page
def index(response):
    return render(response, 'main/index.html')

# dashborad view
def dashboard(response):
    return render(response, 'accounts/dashboard.html')

# products view 
def products(response):
    return render(response, 'main/products.html')

# customer view 
def customers(response):
    return render(response, 'accounts/customer.html')

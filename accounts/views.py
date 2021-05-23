from django.shortcuts import render

# Create your views here.

def index(response):
    return render(response, 'main/index.html')
    
def dashboard(response):
    return render(response, 'accounts/dashboard.html')

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('products/', views.products, name="products"),
    path('customer/<int:pk>/', views.customer, name="customer"),
    path('create_order/', views.create_order, name="creat_order")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

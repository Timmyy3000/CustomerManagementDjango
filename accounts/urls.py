from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_order/<str:pk>/', views.create_order, name="create_order"),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete/<str:pk>/', views.delete_order, name="delete_order"),
    path('create_customer/', views.create_customer, name="create_customer"),
    path('update_customer/<str:pk>', views.update_customer, name="update_customer"),
    path('delete_customer/<str:pk>/', views.delete_customer, name="delete_customer"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('register/', views.register, name = "register"),
    path('profile/', views.user_profile, name = "profile"),

]

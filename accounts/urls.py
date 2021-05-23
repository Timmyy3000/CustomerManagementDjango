from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('',views.index),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('products/', views.products, name="products")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    # Categories
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    
    # Items
    path('items/', views.item_list, name='item_list'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    
    # Customers
    path('customers/', views.customer_list, name='customer_list'),
    
    # Suppliers
    path('suppliers/', views.supplier_list, name='supplier_list'),
    
    # Purchases
    path('purchases/', views.purchase_list, name='purchase_list'),
    
    # Sales
    path('sales/', views.create_sale, name='create_sale'),
]
from django.urls import path
from . import views

urlpatterns = [
  # ========== Category endpoints ==========
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    
     # ========== Item endpoints ==========
    path('items/', views.item_list, name='item_list'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    
    # ========== Customer endpoints ==========
    path('customers/', views.customer_list, name='customer_list'),
    
      # ========== Supplier endpoints ==========
    path('suppliers/', views.supplier_list, name='supplier_list'),
    
       # ========== Purchase endpoints ==========
    path('purchases/', views.purchase_list, name='purchase_list'),
    
    # ========== Sale endpoint ==========
    path('sales/', views.create_sale, name='create_sale'),
]
"""Admin configuration for the inventory app."""
from django.contrib import admin
from .models import Category, Supplier, Customer, Item, Purchase, PurchaseItem, Sale, SaleItem

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Purchase)
admin.site.register(PurchaseItem)
admin.site.register(Sale)
admin.site.register(SaleItem)
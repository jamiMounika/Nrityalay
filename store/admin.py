from django.contrib import admin
from .models import Product, CartItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'added_at')

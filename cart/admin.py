from django.contrib import admin
from .models import CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ('cart', 'game', 'quantity', 'active', 'check')


admin.site.register(CartItem, CartAdmin)
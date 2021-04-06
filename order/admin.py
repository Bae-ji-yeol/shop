from django.contrib import admin
from .models import GameOrder


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'game')


admin.site.register(GameOrder, OrderAdmin)

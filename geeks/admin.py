from django.contrib import admin
from .models import GeeksModel

class GeeksAdmin(admin.ModelAdmin):
    list_display = 'geeks_field'


admin.site.register(GeeksModel)
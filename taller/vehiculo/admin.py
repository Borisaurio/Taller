from django.contrib import admin
from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("patente", "modelo", "año", "dueño")
    search_fields = ("patente", "modelo", "dueño")
    list_filter = ("año",)

from django.contrib import admin
from .models import Mecanico

@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "contacto", "especialidad")
    search_fields = ("nombre", "especialidad")
    list_filter = ("especialidad",)

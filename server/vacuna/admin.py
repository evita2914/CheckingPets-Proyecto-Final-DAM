from django.contrib import admin

# Register your models here.
from .models import Vacuna, FechaVacuna

admin.site.register(Vacuna)
admin.site.register(FechaVacuna)

from django.contrib import admin

# Register your models here.
from .models import Animal, TipoAnimal

admin.site.register(Animal)
admin.site.register(TipoAnimal)
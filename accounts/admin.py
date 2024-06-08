from django.contrib import admin

# Register your models here.
from .models import CustomUser, Veterinaria, CitaMedica, Producto, TipDeCuidado

admin.site.register(CustomUser)
admin.site.register(Veterinaria)
admin.site.register(CitaMedica)
admin.site.register(Producto)
admin.site.register(TipDeCuidado)
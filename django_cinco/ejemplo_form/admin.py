from django.contrib import admin

# Register your models here.
from ejemplo_form.models import Tabla_dos, Tabla_uno


admin.site.register(Tabla_dos)
admin.site.register(Tabla_uno)
from django.contrib import admin

# Register your models here.

from myapp.models import Propietario
from myapp.models import Mascota

class PropietarioAdmin(admin.ModelAdmin):
    pass

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'propietario')
    list_filter = ('propietario',)
    search_fields = ('name',)
    ordering = ('id',)

admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Propietario, PropietarioAdmin)

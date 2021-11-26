from django.contrib import admin

# Register your models here.

from myapp.models import Propietario
from myapp.models import Mascota

class PropietarioAdmin(admin.ModelAdmin):
    pass

class MascotaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Propietario, PropietarioAdmin)

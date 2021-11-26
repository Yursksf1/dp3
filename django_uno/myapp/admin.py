from django.contrib import admin

# Register your models here.

from django.contrib import admin
from myapp.models import Propietario

class PropietarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Propietario, PropietarioAdmin)


from myapp.models import Mascota

class MascotaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mascota, MascotaAdmin)
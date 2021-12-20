from django.contrib import admin

# Register your models here.
from shopers.models import Client, Vehicle


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'address')
    search_fields = ('first_name', 'last_name', 'phone')
    ordering = ('id',)


# TODO: add client referente, and add a day to renovation
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id','type_vehicle', 'registration', 'renovation_date')
    list_filter = ('type_vehicle','renovation_date')
    search_fields = ('registration', 'last_name', '')
    ordering = ('id',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Vehicle, VehicleAdmin)

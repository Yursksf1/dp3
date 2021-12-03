# Django
from django.core.management.base import BaseCommand
from django.utils import timezone
from myapp.models import Mascota, Propietario

# importing datetime module
from datetime import datetime
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):

        path = './myapp/management/commands/data_import.csv'
        is_fitst_row = True 
        count_of_propietario_added = 0
        count_of_mascota_added = 0
        count_of_row = 0

        with open(path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                count_of_row = count_of_row + 1 
                if is_fitst_row:
                    is_fitst_row = False
                else:
                    propietario_data = {
                        'name': row[0]
                    }
                    
                    mascota_data = {
                        'name': row[1],
                    }

                    propietario = Propietario.objects.create(
                        **propietario_data
                    )
                    count_of_propietario_added = count_of_propietario_added + 1


                    mascota_data['propietario'] = propietario
                    Mascota.objects.create(
                        **mascota_data
                    )
                    count_of_mascota_added = count_of_mascota_added + 1

                    

        print('numero de registros en el archivo', count_of_row)
        print('numero de registros de propietario agregados el archivo', count_of_propietario_added)
        print('numero de registros de mascotas agregados el archivo', count_of_mascota_added)


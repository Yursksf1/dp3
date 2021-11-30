# Django
from django.core.management.base import BaseCommand
from django.utils import timezone
from shopers.models import Client, Vehicle

# importing datetime module
from datetime import datetime
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('hola mundo voy a popular data!')
        # /Users/yurley.sanchez/Desktop/yurley/dp3/django_tres/shopers/management/commands/data_import.csv
        path = './shopers/management/commands/data_import.csv'
        is_fitst_row = True 
        count_of_client_added = 0
        count_of_vehicle_added = 0
        count_of_row = 0
        with open(path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                count_of_row = count_of_row + 1 
                if is_fitst_row:
                    is_fitst_row = False
                else:
                    client_data = {
                        'first_name': row[0],
                        'last_name': row[1],
                        'phone': row[2],
                        'address': row[3],
                    }
                    
                    renovation_date = row[7]
                    renovation_date = datetime.strptime(renovation_date, '%d/%m/%y')
                    renovation_date = timezone.make_aware(renovation_date, timezone.get_default_timezone())
                    
                    vehicle_data = {
                        'type_vehicle': row[4],
                        'registration': row[5],
                        'renovation_date': renovation_date,
                    }

                    if not Client.objects.filter(
                            first_name=client_data.get('first_name'),
                            last_name=client_data.get('last_name'),
                            phone=client_data.get('phone'),
                        ).exists():

                        Client.objects.create(
                            **client_data
                        )
                        count_of_client_added = count_of_client_added + 1

                    if not Vehicle.objects.filter(
                            registration=vehicle_data.get('registration')
                        ).exists():

                        client = Client.objects.filter(
                            first_name=client_data.get('first_name'),
                            last_name=client_data.get('last_name'),
                            phone=client_data.get('phone'),
                        ).first()

                        vehicle_data['client_id'] = client
                        Vehicle.objects.create(
                            **vehicle_data
                        )
                        count_of_vehicle_added = count_of_vehicle_added + 1

                    

        print('numero de registros en el archivo', count_of_row)
        print('numero de registros de clientes agregados el archivo', count_of_client_added)
        print('numero de registros de vehiculos agregados el archivo', count_of_vehicle_added)


from django.db import models
from django.contrib import admin

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __srt__(self):
        return self.get_full_name()


class Vehicle(models.Model):
    client_id = models.ForeignKey(
        'Client',
        on_delete=models.CASCADE,
    )
    type_vehicle = models.CharField(
        max_length=1,
        choices=[
            ('C', 'Car'),
            ('M', 'Motorcycle')

        ]
    )
    registration = models.CharField(max_length=10)
    renovation_date = models.DateField()


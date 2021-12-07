from django.db import models

# Create your models here.

class Tabla_uno(models.Model):
    name = models.CharField(
        max_length=100,
        default='Minino',
    )

    def __str__(self):
        return self.name


class Tabla_dos(models.Model):
    name = models.CharField(
        max_length=100,
        default='Minino',
    )

    referencia = models.ForeignKey(
        'Tabla_uno',
        on_delete=models.CASCADE,
        default=None
    )
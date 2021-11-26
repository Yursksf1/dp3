from django.db import models

# Create your models here.

class Propietario(models.Model):
    name = models.CharField(
        max_length=100,
        default='Minino',
    )

    
    def __str__(self):
        return self.name

class Raza(models.Model):
    pass

class TipoMascota(models.Model):
    pass

class Mascota(models.Model):
    name = models.CharField(
        max_length=100,
        default='Minino',
    )
    propietario = models.ForeignKey(
        'Propietario',
        on_delete=models.CASCADE,
        default=None
    )

    def __str__(self):
        return self.name
        
class DatosMedicos(models.Model):
    pass


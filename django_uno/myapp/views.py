from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Mascota, Propietario


# Create your views here.

def index(request):
    message = """
        <a href="mascotas"> mascotas</a> </br>
        <a href="propietairos"> propietairos</a> </br>
    """
    return HttpResponse(message)


def mascotas(request):
    mascotas = Mascota.objects.all()
    message = ""

    for mascota in mascotas:
        message = message + '''
        {} - {} </br>
        '''.format(mascota.name, mascota.propietario.name )
    message = message + """
    </br>
    <a href="../myapp"> atras</a>
    """
    return HttpResponse(message)


def propietairos(request):
    propietatios = Propietario.objects.all()
    message = ""

    for propietairo in propietatios:
        message = message + '''
        {} </br>
        '''.format(propietairo.name)
    message = message + """
        </br>
        <a href="../myapp"> atras</a>
    """
    return HttpResponse(message)


from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Mascota, Propietario


# Create your views here.

def index(request):

    return render(request, template_name='index.html')

def index_example(request):
    message = """
        <a href="mascotas"> mascotas</a> </br>
        <a href="propietarios"> propietarios</a> </br>
    """
    return render(request, template_name='index_example.html')


def mascotas(request):
    params = request.GET
    page = params.get('page')
    numero_de_registros_por_pagina = 10

    mascotas = Mascota.objects.all()
    if page:
        page = int(page)
        inicio = numero_de_registros_por_pagina * (page-1)
        fin = numero_de_registros_por_pagina * (page)
        mascotas = mascotas[inicio:fin]

    message = ""

    for mascota in mascotas:
        message = message + '''
        {} - {} - {} </br>
        '''.format(mascota.id, mascota.name, mascota.propietario.name )
    message = message + """
    </br>
    <a href=".."> atras</a>
    </br>
    <a href="?page={}"> siguiente pagina</a>

    """.format(page+1 if page else 1)
    return HttpResponse(message)


def propietarios(request):
    propietarios = Propietario.objects.all()

    context = {
        'propietarios': propietarios,
        'title': 'Solo propietarios'
    }
    template_name = 'propietarios.html'

    return render(
        request,
        template_name=template_name,
        context=context
    )


# Django
from django.core.management.base import BaseCommand
from django.utils import timezone
from quiz.models import Question, Response

# importing datetime module
from datetime import datetime
import csv


lista_preguntas = [
  '¿Cuál es la capital de Colombia?: ',
  '¿Qué significa ONU?: ',
  '¿Cómo se llama la profe del diplomado?:'
]

lista_respuestas = [
  {
    'a': 'Bogotá',
    'b': 'Barranquilla',
    'c': 'Cali',
    'd': 'Medellín',
    'e': 'Bucaramanga',
    'respuesta': 'a'
  },
  {
    'a': 'Organización de noticias unidas ',
    'b': 'Organo nacional unilateral',
    'c': 'Organización de naciones unidas',
     'respuesta': 'c'
  },
  {
    'a': 'Laura',
    'b': 'Tatiana',
    'c': 'Yurley',
    'respuesta': 'c'
  }
]


class Command(BaseCommand):
    def handle(self, *args, **options):

        for index, row in enumerate(lista_preguntas):
            q = Question()
            q.description = row
            q.save()

            for key, response in lista_respuestas[index].items():
                if key != 'respuesta':
                    r = Response()
                    r.description = response
                    r.question = q
                    if lista_respuestas[index]['respuesta'] == key:
                        r.is_correct_answer = True
                    r.save()


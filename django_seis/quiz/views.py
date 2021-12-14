from django.shortcuts import render
from quiz.models import Question, Response
# Create your views here.

def show_index(request):
    reponses = Response.objects.all()

    questions = Question.objects.all()
    context = {
        'reponses': reponses,
        'questions': questions,
    }
    return render(
        request,
        'index.html',
        context
    )

def check_response(request):
    print(request.POST)
    print('''
    TODO: validar las preguntas con las repuesta. 
    pregunta_4: 15
    donde 4 es el id de la pregunta y el 
    15 es el id de la respuesta 
    en el objeto respuesta hay un atributo de 'is_correct_answer' si este es true, entonces la respuesta es correcta 
    ''')

    # q = Question.objects.filter(id=4)
    # r = Response.objects.filter(id=15)
    # if r.is_correct_answer:
    #     print('some')

    return render(
        request,
        'index.html',
    )
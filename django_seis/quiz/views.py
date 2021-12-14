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
    print('envio la respuestas')
    return render(
        request,
        'index.html',
    )
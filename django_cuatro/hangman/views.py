from django.shortcuts import render
from .models import Word
import math

# Create your views here.

# view base on function
def index_funcion(request):
    cant_words = Word.objects.count()
    current_word = Word.objects.filter(id=math.random(cant_words))
    print(current_word.hidden_word)
    list_char = [
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                "L", "M", "N",  "O", "P", "Q", "R", "S", "T", "U", "V",
                "W", "X", "Y", "Z"
    ]
    context = {
        'current_word': current_word,
        'list_char': list_char
    }
    return render(request, 'hangman/base.html', context)


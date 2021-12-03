from django.shortcuts import render
from django.http import JsonResponse

from .models import Word
import random

# Create your views here.

# view base on function

def index_funcion(request):
    cant_words = Word.objects.count()
    current_word = Word.objects.filter(id=random.random() * cant_words).first()
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
    return render(request, 'hangman/index.html', context)



def game_turn(request):
    data = {}
    if request.method == 'POST':
        payload = request.POST
        id = payload.get('id')
        choise = payload.get('choise')

        current_word = Word.objects.filter(id).first()
        hidden_word = current_word.hidden_word
        spaces = "_" * len(hidden_word)
        data['is_valid'] = False

        if choise in hidden_word:
            spaces = ""
            data['is_valid'] = True
            for w in hidden_word:
                if w.upper() == choise:
                    spaces = spaces + " {} ".format(w)
                else:
                    spaces = spaces + ' _ '

        data['new_word'] = spaces

    return JsonResponse(data)

    cant_words = Word.objects.count()
    current_word = Word.objects.filter(id=random.random() * cant_words).first()
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


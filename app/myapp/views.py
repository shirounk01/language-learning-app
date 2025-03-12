from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
import random


# Create your views here.
def home_page(request):
    return render(request, "base.html")


def definition_page(request):
    definition = request.GET.get("definition")
    word = Word.objects.all().filter(name=definition).first()
    return render(request, "word_definition.html", {"word": word})


def dictionary(request):

    page = request.GET.get("page")
    pos_filter = request.GET.get("pos")

    pos = {pos[1]: pos[0] for pos in Word.PART_OF_SPEECH}

    words_list = (
        Word.objects.filter(part_of_speech=pos[pos_filter])
        if pos_filter
        else Word.objects.all()
    )
    p = Paginator(words_list, 2)
    words = p.get_page(page)

    return render(
        request,
        "dictionary.html",
        {"words": words, "parts_of_speech": pos.keys},
    )


def quiz(request):
    quiz_words = random.sample(list(Word.objects.all()), k=3)
    return render(request, "type_quiz.html", {"words": quiz_words})

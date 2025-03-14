from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

import random
import base64
import json
import urllib.parse


# Create your views here.
def home_page(request):
    return render(request, "base.html")


def definition_page(request):
    definition = request.GET.get("definition")
    word = Word.objects.all().filter(name=definition).first()
    if not word:
        word = Word.objects.all().filter(translation=definition).first()
    return render(request, "word_definition.html", {"word": word})


def dictionary(request):
    if not len(request.GET):
        del request.session["previous_filter"]

    pos = {pos[1]: pos[0] for pos in Word.PART_OF_SPEECH}

    def retrieve_data(filter):
        if filter in list(pos.keys()):
            return Word.objects.filter(part_of_speech=pos[filter])
        else:
            return Word.objects.all()

    page = request.GET.get("page")

    pos_filter = request.GET.get("pos")
    if pos_filter == None:
        pos_filter = request.session.pop("previous_filter", None)

    words_list = retrieve_data(pos_filter)
    p = Paginator(words_list, 2)
    words = p.get_page(page)

    request.session["previous_filter"] = pos_filter

    return render(
        request,
        "dictionary.html",
        {"words": words, "parts_of_speech": pos.keys},
    )


def quiz_selection(request):
    return render(request, "quiz_selection_page.html")


def quiz_end_screen(request):
    return render(request, "quiz_end_screen.html")


def quiz(request):
    data = list((request.GET.dict().keys()))[0]
    try:
        data = urllib.parse.unquote(data)
        decoded_json = base64.b64decode(data).decode("utf-8")
        quiz_info_json = json.dumps(urllib.parse.parse_qs(decoded_json))
        quiz_info = dict(json.loads(quiz_info_json))
        quiz_type = quiz_info["quiz-type"][0]
        question_number = int(quiz_info["question-number"][0])
        question_translation = quiz_info["question-translation"][0]
    except Exception as e:
        print(">>>", e)
    print(question_number)
    quiz_words = random.sample(list(Word.objects.all()), k=question_number)

    if question_translation == "en":
        for word in quiz_words:
            word.name, word.translation = word.translation, word.name
    elif question_translation == "mix":
        random_indexes = random.sample(range(len(quiz_words)), k=len(quiz_words) // 2)
        for index in random_indexes:
            quiz_words[index].name, quiz_words[index].translation = (
                quiz_words[index].translation,
                quiz_words[index].name,
            )

    if quiz_type == "type":
        return render(request, "type_quiz.html", {"words": quiz_words})
    elif quiz_type == "choice":
        pass

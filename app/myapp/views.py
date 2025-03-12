from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def home_page(request):
    return render(request, "base.html")


def definition_page(request):
    definition = request.GET.get("definition")
    word = Word.objects.all().filter(name=definition).first()
    return render(request, "word_definition.html", {"word": word})


def dictionary(request):
    p = Paginator(Word.objects.all(), 2)
    page = request.GET.get("page")
    words = p.get_page(page)
    return render(request, "dictionary.html", {"words": words})

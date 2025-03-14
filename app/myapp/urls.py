from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("search", views.definition_page, name="definition"),
    path("dictionary", views.dictionary, name="dictionary"),
    path("quiz_end_screen", views.quiz_end_screen, name="quiz_end_screen"),
    path("quiz_selection", views.quiz_selection, name="quiz_selection"),
    path("quiz", views.quiz, name="quiz"),
]

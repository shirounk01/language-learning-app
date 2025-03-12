from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("search", views.definition_page, name="definition"),
    path("dictionary", views.dictionary, name="dictionary"),
]

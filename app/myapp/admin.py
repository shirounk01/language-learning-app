from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Word)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = (
        "word",
        "translation",
        "part_of_speech",
        "gender",
        "conjugation",
    )
    list_filter = ("part_of_speech", "gender", "conjugation")

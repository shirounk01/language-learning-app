from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Word)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "translation",
        "part_of_speech",
        "gender",
        "conjugation",
        "required_case",
    )
    list_filter = ("part_of_speech", "gender", "conjugation")

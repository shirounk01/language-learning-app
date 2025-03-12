from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class Word(models.Model):

    class Meta:
        ordering = ["id"]

    PART_OF_SPEECH = (
        ("N", "Noun"),
        ("V", "Verb"),
        ("Adj", "Adjective"),
        ("Adv", "Adverb"),
        ("Exp", "Expression"),
    )

    GENDER = (
        ("M", "Masculine"),
        ("F", "Feminine"),
        ("N", "Neuter"),
    )

    NUMBER = (
        ("SG", "Singular"),
        ("PL", "Plural"),
    )

    CONJUGATION = (
        ("I", "I"),
        ("II", "II"),
        ("III", "III"),
        ("IV", "IV"),
    )

    CASES = (
        ("Nom", "Nominative"),
        ("Gen", "Genitive"),
        ("Dat", "Dative"),
        ("Acc", "Accusative"),
        ("Instr", "Instrumental"),
        ("Loc", "Locative"),
        ("Voc", "Vocative"),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    part_of_speech = models.CharField(max_length=3, choices=PART_OF_SPEECH)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
    number = models.CharField(max_length=10, choices=NUMBER, default="SG")
    conjugation = models.CharField(
        max_length=3, choices=CONJUGATION, blank=True, null=True
    )
    required_case = MultiSelectField(
        max_length=100, choices=CASES, max_choices=3, blank=True, null=True
    )

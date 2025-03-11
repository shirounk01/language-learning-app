from django.db import models


# Create your models here.
class Word(models.Model):

    PART_OF_SPEECH = {
        "N": "Noun",
        "V": "Verb",
        "Adj": "Adjective",
        "Adv": "Adverb",
        "Exp": "Expression",
    }

    GENDER = {"M": "Masculine", "F": "Feminine", "N": "Neuter"}

    CONJUGATION = {
        "I": "I",
        "II": "II",
        "III": "III",
        "IV": "IV",
    }

    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    part_of_speech = models.CharField(max_length=3, choices=PART_OF_SPEECH)
    gender = models.CharField(
        max_length=10, choices=PART_OF_SPEECH, blank=True, null=True
    )
    conjugation = models.CharField(
        max_length=3, choices=CONJUGATION, blank=True, null=True
    )

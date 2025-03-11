from django.db import models


# Create your models here.
class Word(models.Model):

    PART_OF_SPEECH = {"N": "Noun", "V": "Verb", "Adj": "Adjective"}

    word_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=200)
    part_of_speech = models.CharField(max_length=3, choices=PART_OF_SPEECH, default="N")

from django.db import models
from django.conf import settings


class Word(models.Model):
    word = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    example = models.TextField(blank=True, null=True)
    sentenceTranslation = models.TextField(blank=True, null=True)
    mnemonic = models.TextField(blank=True, null=True)
    oxford_list = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.word


class UserWordProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    known = models.BooleanField(default=False)
    lastLearned = models.IntegerField(default=0)
    correctAnswersCount = models.IntegerField(default=0)
    repetitionInterval = models.IntegerField(default=2)
    lastCorrectAnswerDate = models.DateField(null=True, blank=True)
    mnemonic = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'word')  # Verhindert doppelte Einträge für einen Benutzer und ein Wort
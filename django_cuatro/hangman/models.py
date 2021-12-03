from django.db import models

# Create your models here.


class Word(models.Model):
    hidden_word = models.CharField(
        max_length=200,
        default='Sample',
    )
    clue = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.hidden_word
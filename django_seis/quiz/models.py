from django.db import models

# Create your models here.


class Question(models.Model):
    description = models.CharField(max_length=300)


class Response(models.Model):
    description = models.CharField(max_length=300)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct_answer = models.BooleanField(default=False)

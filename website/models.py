from django.db import models

class Quiz (models.Model):
    question = models.ForeignKey('Question')
    answer = models.CharField (max_length=150)

class Question (models.Model):
    question = models.CharField(max_length=200)



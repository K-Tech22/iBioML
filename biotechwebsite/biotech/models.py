from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)


class QuestionFile(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    file = models.FileField(upload_to='questions_files/')


class AnswerFile(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    file = models.FileField(upload_to='answers_files/')

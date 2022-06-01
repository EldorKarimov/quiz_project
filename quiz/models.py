from django.db import models
from accounts.models import CustomUser


class QuizModel(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Answer(models.Model):
    name = models.CharField(max_length=128)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Result(models.Model):
    number_of_question = models.IntegerField()
    correct_question = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
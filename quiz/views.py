from django.shortcuts import render
from .models import QuizModel, Question, Answer, Result


def home(request):
    quizs = QuizModel.objects.all()
    context = {
        'quiz':quizs,
    }
    return render(request, 'quiz/quiz.html', context)

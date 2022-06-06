from django.shortcuts import render

from accounts.models import CustomUser
from .models import QuizModel, Question, Answer, Result
from django.contrib.auth.decorators import login_required
from random import shuffle, sample

def home(request):
    quizs = QuizModel.objects.all().order_by('-pk')
    context = {
        'quiz':quizs,
    }
    return render(request, 'quiz/quiz.html', context)

@login_required(login_url='login')
def quiz_test(request, pk):
    questions = Question.objects.filter(quiz_id=pk)
    questions = sample(list(questions), 3)
    answers = Answer.objects.all()
    answers = list(answers)
    shuffle(answers)
    if request.method == 'POST':
        correct = 0
        wrong = 0
        for q in questions:
            if request.POST.get(q.name) == 'True':
                correct += 1
            else:
                wrong += 1
            quiz = q.quiz
        Result.objects.create(
            user=CustomUser.objects.get(username=request.user.username),
            number_of_question=len(questions),
            correct_question=correct,
            quiz=quiz
        )

        context = {
            'correct':correct,
            'wrong':wrong,
            'total_question':len(questions),
            'total': round(correct * 100 / len(questions), 2)
        }
        return render(request, 'quiz/result.html', context)
    context = {
        'questions': questions,
        'answers':answers
    }
    return render(request, 'quiz/quiz_test.html', context)
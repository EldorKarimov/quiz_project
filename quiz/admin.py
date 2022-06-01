from django.contrib import admin
from .models import QuizModel, Question, Answer, Result

@admin.register(QuizModel)
class QuizModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug":['name']}

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['name', 'is_right']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name', 'quiz']
    inlines = [AnswerInlineModel]



@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['number_of_question', 'correct_question', 'datetime']
from django.shortcuts import render
from .models import QuestionModel, AnswerModel, CategoryModel

# Create your views here.
def question(request):
    question = QuestionModel.objects.all()
    return render(request, 'question.html',{'question':question})

def popular(request):
    popularqs = QuestionModel.objects.filter(q_votes__gt = 2)
    return render(request, 'popular.html', {'popularqs':popularqs})
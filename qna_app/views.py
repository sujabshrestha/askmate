from django.shortcuts import render, redirect
from .models import QuestionModel, AnswerModel, CategoryModel
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
# Create your views here.
def questionmodel_list(request):
    question = QuestionModel.objects.all()
    return render(request, 'questionmodel_list.html',{'question':question})

def popular(request):
    popularqs = QuestionModel.objects.filter(question_votes__gt = 2)
    return render(request, 'popular.html', {'popularqs':popularqs})

def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('qna:read')
            except:
                return HttpResponse('Failed')
        else:
            print(form.errors)
            return HttpResponse('Form not Valid!')       
    else:    
        category = CategoryModel.objects.all()
        return render(request,'questionmodel_create.html',{'category':category})

def update_question(request,id):
    question = QuestionModel.objects.get(id=id)
    if request.method == "POST":
        form = QuestionForm(request.POST,request.FILES,instance=question)
        if form.is_valid():
            try:
                form.save()
                return redirect('qna:read')
            except:
                return HttpResponse('Failed')
        else:
            print(form.errors)
            return HttpResponse('Form not Valid!')       
    else:    
        form = QuestionForm(instance=question)
        return render(request,'questionmodel_update.html',{'form':form})      

def delete_question(request,id): 
    question = QuestionModel.objects.get(id=id)
    question.delete()
    return redirect('qna:read')

def vote_qn(request,id):
    q = QuestionModel.objects.get(id=id)
    q.question_votes=q.question_votes + 1
    q.save()
    return redirect('qna:read')

def answer(request,id):
    if request.method == "POST":
        by = request.POST.get('answer_by')
        desc = request.POST.get('answer_description')
        img = request.POST.get('answer_img')
        q = QuestionModel.objects.get(id=id)
        comment =AnswerModel(answer_by=by, answer_description=desc, answer_img=img,question=q)
        comment.save()
        return redirect('qna:read')

    else:
        form = AnswerForm
        a = {'form':form}
        b = {'id':id}
        c = {**a,**b}
        return render(request, 'answermodel_create.html',c)

class QuestionListView(ListView):
    queryset = QuestionModel.objects.all()

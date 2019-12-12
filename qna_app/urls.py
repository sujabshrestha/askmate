"""askmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from qna_app import views
app_name = 'qna'

urlpatterns = [
    
    path('popular/',views.popular),
    path('read/',views.questionmodel_list,name='read'),
    path('add/',views.add_question,name='add'),
    path('update/<int:id>/',views.update_question,name='update'),
    path('delete/<int:id>/',views.delete_question,name='delete'),
    path('vote/<int:id>',views.vote_qn,name='vote'),
    path('ans/<int:id>',views.answer,name='ans'),
    path('listview/',views.QuestionListView.as_view(),name="qnlist")

]

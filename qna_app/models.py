from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()

    
    def __str__(self):
        return (self.title)


class QuestionModel(models.Model):
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=120)
    timestamp =models.DateTimeField(auto_now_add=True)
    question_desc = models.TextField()
    question_votes = models.IntegerField(default=0)
    question_img = models.ImageField(upload_to='QuestionImg',blank=True,null=True)

    def __str__(self):
        return(self. title)

class AnswerModel(models.Model):
    timestamp =models.DateTimeField(auto_now_add=True)
    answer_votes = models.IntegerField(default=0)
    answer_by = models.CharField(max_length=120)
    answer_description = models.TextField()
    answer_img = models.ImageField(upload_to='answer_img',blank=True,null=True)
    is_accept = models.BooleanField(default=0)
    question = models.ForeignKey(QuestionModel,on_delete=models.CASCADE)

    def __str__(self):
        return(self.answer_description[:50]+'.....')



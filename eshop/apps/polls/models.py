import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    length = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    editor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='edited_questions')
    is_sold = models.BooleanField(default=False)
    
    def __str__(self):
        return "{} published at {}".format(self.question_text, self.pub_date)
        
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class QuestionEditors(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    editor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='questions')
    type = models.CharField(max_length=200)#with choises editor|aauthor
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_description = models.CharField(max_length=200, default='')
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

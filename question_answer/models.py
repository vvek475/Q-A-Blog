from django.db import models
from category.models import Category


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    added_date = models.DateTimeField()
    
    
    def __str__(self):
        return str(self.question)
        
        
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    added_date = models.DateTimeField()
    up_voting = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    
    
    def __str__(self):
        return str(self.answer)
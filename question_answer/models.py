from django.db import models
from category.models import Category


class Question(models.Model):
    """ Question Model Class """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    added_date = models.DateTimeField()
    
    """ 
        Return a object representation string. Model Object PK to Question. 
        example Question Object (1) to Which is good movie to watch? 
    """    
    def __str__(self):
        return str(self.question)
        
        
class Answer(models.Model):
    """ Answer Model Class """
    # Question PK Refrence as FK because questions can have multiple answers
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    answer = models.TextField()
    added_date = models.DateTimeField()
    up_voting = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    
    
    """ 
        Return a object representation string. Model Object PK to Answer. 
        example Answer Object (1) to Watch XYZ movie. 
    """  
    def __str__(self):
        return str(self.answer)
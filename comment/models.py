from django.db import models
from question_answer.models import Question


class Comment(models.Model):
    """ Comment Model Class """
    # Question PK Refrence as FK because questions can have multiple comments
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comments = models.CharField(max_length=255)
    image = models.ImageField(upload_to='comments', null=True, blank=True)
    added_date = models.DateTimeField()

    """ 
        Return a object representation string. Model Object PK to Comment. 
        example Comment Object (1) to XYZ Comment? 
    """    
    def __str__(self):
        return str(self.comments)

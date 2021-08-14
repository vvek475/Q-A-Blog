from django.db import models
from question_answer.models import Question


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comments = models.CharField(max_length=255)
    image = models.ImageField(upload_to='comments', null=True, blank=True)
    added_date = models.DateTimeField()

    
    def __str__(self):
        return str(self.comments)

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.title)
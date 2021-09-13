from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
# Create your models here.
class UserProfile(models.Model):
    user=ForeignKey(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    mobile_no=models.CharField(null=True,blank=True,max_length=255)

    def __str__(self):
        return str(self.user)
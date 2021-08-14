from django.contrib import admin
from . models import Question, Answer


class Admin(admin.ModelAdmin):
    list_display = ['question', 'category', 'status', 'added_date']
    list_filter = ('status', 'added_date')
    
    
admin.site.register(Question, Admin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'added_date', 'up_voting', 'down_vote']
admin.site.register(Answer, AnswerAdmin)

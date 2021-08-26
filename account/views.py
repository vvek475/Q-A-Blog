from django.shortcuts import render
from category.models import Category
from question_answer.models import Question, Answer


""" Home page view function """
def homePage(request):
    navigation_categories = Category.objects.filter(status=True).order_by('-id')[:5]
    categories = Category.objects.filter(status=True)
    questions = Question.objects.filter(status=True).order_by('-id')[:5]
    return render(request, 'home.html', {
                                        'navigation_categories':navigation_categories,
                                        'categories' : categories,
                                        'questions':questions})
                                        

def categoryQuestion(request, category_id):
    navigation_categories = Category.objects.filter(status=True).order_by('-id')[:5]
    categories = Category.objects.filter(status=True)
    questions = Question.objects.filter(status=True, category_id=category_id)
    return render(request, 'category-question.html', {
        'navigation_categories': navigation_categories,
        'categories' : categories,
        'questions' : questions
    })
    
def QuestionDetails(request, question_id):
    navigation_categories = Category.objects.filter(status=True).order_by('-id')[:5]
    answers = Answer.objects.filter(question_id=question_id)
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        question = {}
    return render(request, 'question-details.html', {
        'navigation_categories': navigation_categories,
        'question':question,
        'answers' : answers
    })
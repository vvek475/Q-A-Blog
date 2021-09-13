from django.contrib.messages.api import success
from django.db import reset_queries
from comment.models import Comment
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from category.models import Category
from question_answer.models import Question, Answer
from user_profile.models import UserProfile
from django.contrib import  messages
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

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
    answersobject = Answer.objects.filter(question_id=question_id)
    answers={}
    for key,answer in enumerate(answersobject):
        comments=Comment.objects.filter(answer=answer)
        try:
            UserProfileobject=UserProfile.objects.get(user=answer.user)
        except UserProfile.DoesNotExist:
            UserProfileobject={}
        answers[key]={
            'answer':answer,
            'user_profile':UserProfileobject,
            'comments':comments
        }
        print(answers[key]['answer'])
        
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        question = {}
    return render(request, 'question-details.html', {
        'navigation_categories': navigation_categories,
        'question':question,
        'answers' : list(answers.values()),
    })

def SaveComment(request):
    questionid = request.POST['question_id']
    answerId=request.POST['answer_id']
    comment=request.POST['comment']
    image=request.FILES.get('image')
    if comment:
        Comment.objects.create(
            answer_id=answerId,
            comments=comment,
            added_date=datetime.now(),
            user=request.user,
            image=image
        )
        messages.success(request,'comment added')
    else:
        messages.error(request,'comment can not be empty')
    return redirect('QuestionDetails',question_id=questionid)

def userRegistration(request):
    if request.method == 'POST':
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        userName =request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        checkUsername =User.objects.filter(username=userName)
        print(userName)
        if checkUsername:
            messages.error(request,'Username already taken')
            print('1')
            return redirect('userRegistration')
            
        else:
            if password == ' ':
                messages.error(request,'password is required')
                print('2')
                return redirect('userRegistration')
            elif confirm_password == ' ':
                messages.error(request,'confirm_password is required')
                print('3')
                return redirect('userRegistration')
            elif password != confirm_password:
                messages.error(request,'password and confirm_password not saame')
                print('4')
                return redirect('userRegistration')
            else:
                print('5')
                user=User.objects.create(
                    first_name=firstname,
                    last_name=lastname,
                    username =userName,
                )
                user.set_password(password)
                user.save()

                messages.success(request,'account created')
                return redirect('userLogin')

    else:
        navigation_categories = Category.objects.filter(status=True).order_by('-id')[:5]
        return render(request,'user-registration.html',{'navigation_categories': navigation_categories,})

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('homePage')
        else:
            messages.error(request, 'Invalid Username or password')
            return redirect('userLogin')
    else:
        navigation_categories = Category.objects.filter(status=True).order_by('-id')[:5]
        return render(request, 'user-login.html', {
            'navigation_categories':navigation_categories,
        })

def userProfile(request):
    return render(request,'user-profile.html')


def postQuestion(request):
    categories = Category.objects.filter(status=True)
    if request.method == 'POST':
        print(request.POST.get('category'))
        question=request.POST.get('question')
        category=request.POST.get('category')
        category_id=Category.objects.get(title=category)
        user=request.user.username
        users=User.objects.get(username=user)
        if question != ' ':
            if len(question)<20:
                messages.error(request,'question too short')
                return redirect('postQuestion')
            elif len(question)>400:
                messages.error(request,'question too long')
                return redirect('postQuestion')
            
            else:
                Question.objects.create(
                    category=category_id,
                    user=users,
                    question=question,
                    added_date=datetime.now()
                )
                messages.error(request,'question has been posted')
                return redirect('homePage')

    navigation_categories = Category.objects.filter(status=True).order_by('-id')[:5]
    return render(request,'post-questions.html',{'navigation_categories': navigation_categories,'categories':categories})

def myQuestions(request):
    user=request.user.username
    users=User.objects.get(username=user)
    questions=Question.objects.filter(user=users)
    print(questions)
    return render(request,'my-questions.html',{'questions':questions,'users':users.username})
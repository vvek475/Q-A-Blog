from django.urls import path
from . import views

""" Url Pattern for root URL Pattern """
urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('category/<int:category_id>', views.categoryQuestion, name='categoryQuestion'),
    path('question/<int:question_id>', views.QuestionDetails, name='QuestionDetails'),
    path('savecomment',views.SaveComment,name="SaveComment"),
    path('add-answer',views.addAnswer,name="add-answer"),
    path('user-registration',views.userRegistration,name="userRegistration"),
    path('user-login',views.userLogin,name='userLogin'),
    path('user-profile',views.userProfile,name='userProfile'),
    path('post-question',views.postQuestion,name='postQuestion'),
    path('my-questions',views.myQuestions,name='myQuestions'),
    path('user-logout',views.logout_view,name='user-logout'),
]
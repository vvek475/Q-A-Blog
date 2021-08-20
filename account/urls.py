from django.urls import path
from . import views

""" Url Pattern for root URL Pattern """
urlpatterns = [
    path('', views.homePage, name="homePage")    
]
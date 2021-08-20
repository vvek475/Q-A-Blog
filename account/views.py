from django.shortcuts import render


""" Home page view function """
def homePage(request):
    return render(request, 'home.html')
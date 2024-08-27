from django.http import HttpResponse
from django.shortcuts import render 

def index(request) :
    return HttpResponse('''Congratulations, You have created a web application using django''')
def home(request) :
    return HttpResponse("Hello")

def homepage(request) :
    return render(request, 'home.html')

# Create your views here.

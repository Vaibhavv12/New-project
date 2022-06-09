from ast import Return
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    return render(request,'home/contact.html')

def register(request):
    return render(request,'home/register.html')

def stulogin(request):
    return render(request,'home/stulogin.html')    

def admlogin(request):
    return render(request,'home/admlogin.html')                    
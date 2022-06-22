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
    return render(request,'authentication/signup.html')

def stulogin(request):
    context  = {'student' : 1}
    return render(request,'authentication/signin.html',context)    

def admlogin(request):
    context  = {'student' : 0}
    return render(request,'authenticaion/signin.html',context)                    
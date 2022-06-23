from django.shortcuts import render

# Create your views here.
from base64 import urlsafe_b64decode
from email import message
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from numpy import roll
from sqlalchemy import true
from . tokens import generate_tokens
from email.message import EmailMessage
from .models import userTable
from time import gmtime, strftime
showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())


# Create your views here.



def home(request):
    return render(request,"authentication/index.html")

def home(request):
    return render(request,"authentication/index.html")


def AddInfo(request):
    if request.method == "POST":
        hscmarks = request.POST['hscmarks']
        sscmarks = request.POST['sscmarks']
        cetscore = request.POST['cetscore']
        lss = request.POST['lss']
        address = request.POST['address']
        gender = request.POST['gender']
        disability = request.POST['disability']
        DOB = request.POST['DOB']
        hostel = request.POST['hostel']
        room = request.POST['room']
        presentyear = request.POST['presentyear']
        studentinfo = userTable.objects.filter(user_id = request.user).update(user_hscmarks=hscmarks, user_sscmarks=sscmarks,user_disability=disability, user_LastSemScore='12',user_cetscore=cetscore,user_address=address,user_gender=gender, user_DOB=DOB, user_is_requested=1,user_hostel=hostel,user_room=room, user_presentyear=presentyear)

        students = userTable.objects.filter(user_id = request.user,is_student=1)
                # print(students.user_DOB)
                
        context = {
            'students' : students
        }
        return render(request, 'authentication/student.html', context)

    return render(request,"authentication/info.html")



def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! Please try another one")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request,"ermail already exist! Please try another one")
            return redirect('home')

        if len(username)>20:
            messages.error(request, "Username must be under 10 characters")

        if pass1 != pass2:
            messages.error(request,"Password does not match")    

        if not username.isalnum():
            messages.error(request,"Username must ne alphanumeric!")
            return redirect('home')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        studentinfo = userTable.objects.create(user_id = username,is_student=True,is_verified=True, user_DOB="",user_LastSemScore=0,user_presentyear="",user_address="",user_name=fname,user_hscmarks=0, user_sscmarks=0,user_disability="", user_is_requested=0,user_hostel="-",user_room="-")
        studentinfo.save()


        messages.success(request, "Your account has been successfully created. We have sent you a confirmation message please confirm your account")


         #welcome email
        # subject = "Welcome to Hostel !!"
        # message = "Hello " + myuser.first_name +"!! \n" + "Welcome to WCE Hostel!! \n Thank you  for visiting our website \n WE have sent you a conformation email, please confirm your email adress in order to activate your account. \n\n Thank you" 
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject,message,from_email,to_list,fail_silently=True)


        #email address confirmation email

        # current_site = get_current_site(request)
        # email_subject = "Confirm your email @ authdemolast!!"
        # message2 = render_to_string('email_confirmation.html',
        # {
        #     'name':myuser.first_name,
        #     'domain' : current_site.domain,
        #     'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token' : generate_tokens.make_token(myuser)
        # })
        # email = EmailMessage(
        #     email_subject,
        #     message2,
        #     settings.EMAIL_HOST_USER,
        #     [myuser.email],
        # )
        # email.fail_silently = True
        # email.send()

        return redirect('/auth/signin/')

    return render(request,"authentication/signup.html")



def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        print(username)
        print(pass1)
        user = authenticate(username=username,password=pass1)
   
        print(request.user)
        if user is not None:
            login(request, user)
            if userTable.objects.filter(user_id = request.user,is_student='1').exists():
                print(1)
                print("success")
                students = userTable.objects.filter(user_id = request.user,is_student=1)
                # print(students.user_DOB)
                
                context = {
                    'students' : students
                }
                return render(request, 'authentication/student.html', context)
            elif userTable.objects.filter(user_id = request.user,is_student= '0').exists():
                print(2)
                print("success")
                students = userTable.objects.filter(is_student = 1, user_is_requested=1)
                # print(students.user_DOB)
                context = {
                    'students' : students
                }
                return render(request, 'authentication/rector.html', context)
            else: 
                print(3)

        else:
            messages.error(request,"Bad Credentials!!!")  
            return redirect('home') 

    return render(request,"authentication/signin.html") 


def StudentsLogin(request):
    userTable = userTable.objects.filter(User_id = request.user, is_student=1)
    print(userTable.user_DOB)
    context = {
        'students' : userTable
    }
    return render(request, 'student.html', context)

def RectorLogin(request):
    userTable = userTable.objects(User_id = '')
    print(userTable.user_DOB)
    context = {
        'students' : userTable
    }
    return render(request, 'rector.html', context)    

def signout(request):
   logout(request)
   messages.success(request,"Logged out Successfully!!")
   return redirect('/')



def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_b64decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_tokens.check_token(myuser,token):
        myuser.is_active = True 
        myuser.save()
        login(request,myuser)
        return redirect('home')
    else:
       return render(request,'activation_failed.html')
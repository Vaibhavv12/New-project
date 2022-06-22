from atexit import register
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name="home"),
    path("home/about/",views.about, name="AboutManagement"),
    path("home/contact/",views.contact, name="ContactUs"),
    path("home/register/",views.register, name="Registation"),
    path("home/stulogin/",views.stulogin, name="StudentLogin"),
    path("home/admlogin/",views.admlogin, name="AdminLogin")

]
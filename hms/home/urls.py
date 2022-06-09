from atexit import register
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name="Homehome"),
    path("about/",views.about, name="AboutManagement"),
    path("contact/",views.contact, name="ContactUs"),
    path("register/",views.register, name="Registation"),
    path("stulogin/",views.stulogin, name="StudentLogin"),
    path("admlogin/",views.admlogin, name="AdminLogin")

]
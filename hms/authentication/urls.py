from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('student/',views.StudentsLogin,name='student'),
    path('rector/',views.RectorLogin,name='rector'),
    path('info/',views.AddInfo,name='info'),
    path('activate/<uid64>/<token>',views.activate, name="activate"),
]
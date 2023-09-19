from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('home/',views.index, name ='index'),
    path('feed/',views.feed, name ='feed'),
    path('contactus/', views.contactus, name='contactus'),
    path('register/',views.register, name = "register"),
    path('login/',views.login, name ='login'),
    path('calc/',views.calc, name='calc'),
    path('logout/',views.logout, name='logout'),
    path('meal/',views.meal,name='meal'),
    path('injury/',views.injury,name='injury'),
    path('profile/',views.profile, name='profile'),
    path('feedback1/',views.feedback1,name='feedback1'),
    path('cricket/',views.cricket,name ='cricket'),
    path('hockey/',views.hockey,name ='hockey'),
    path('football/',views.football,name ='football'),
    path('basketball/',views.basketball,name ='basketball'),
    path('invalid/',views.invalid,name='invalid')
]

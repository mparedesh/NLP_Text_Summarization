from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index,name='Home'),
    path('url',views.url,name='url'),
    path('text',views.text,name='Text'),
    path('fileUpload',views.fileUpload,name='FileUpload'),
    path('textFromImage',views.textFromImage,name='textFromImage'),
    path('contact',views.contactUs,name='contact'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('loginlogoutbutton',views.loginlogoutbutton,name='loginlogoutbutton'),
    path('registeration',views.registeration,name='registeration'),
    path('summaryhistory',views.summaryhistory,name='summaryhistory')

]

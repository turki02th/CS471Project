#from django import views 
from django.urls import path ;import include
from apps.bookmodule import views

urlpatterns = [

    path('',views.index,name='index')
]


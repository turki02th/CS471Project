#from django import views 
from django.urls import path ;import include
from apps.bookmodule import views

from django.urls import path
from django.urls import re_path
from apps.bookmodule import views


urlpatterns = [    
    path('', views.index, name='index'),
    path('books', views.books),
    path('book/<int:bId>', views.book)
]
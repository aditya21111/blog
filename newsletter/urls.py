from django.contrib import admin
from django.urls import path,include
from django.urls import include, re_path
from . import views



urlpatterns = [
    path("subscribe",views.subscribe,name='subscribe'),
    path("unsubscribe",views.unsubscribe,name='unsubscribe'),
    
   
]
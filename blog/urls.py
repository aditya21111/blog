from django.contrib import admin
from django.urls import path
from . import views

app_name ='blog'


urlpatterns = [
    path("",views.blogHome,name='blogHome'),
    path("postComment",views.postComment,name='postComment'),
    path("<str:slug>/",views.blogPost,name='blogPost'),
    path("tag/<str:tag>/",views.tagfilter,name="tagfilter")
   
    
]

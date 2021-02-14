from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("contact/",views.contact,name='contact'),
    path("about",views.about,name='about'),
    path("search",views.search,name='search'),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.logout,name="logout"),
    path("profile/",views.profile,name="profile")
    
]
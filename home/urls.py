from django.contrib import admin
from django.urls import path,include
from django.urls import include, re_path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path("contact/",views.contact,name='contact'),
    path("about",views.about,name='about'),
    path("search",views.search,name='search'),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.logout,name="logout"),
    path('accounts/', include('allauth.urls')),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')), 
    
    re_path('^', include('django.contrib.auth.urls')),
    path("profile/",views.profile,name="profile"),
]
    
    

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
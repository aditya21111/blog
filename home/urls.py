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
    
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("profile/",views.profile,name="profile")
]
    
    

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
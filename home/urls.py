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
    re_path(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    re_path(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.password_reset_confirm, name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'), # <--
    
    path("profile/",views.profile,name="profile")
    
]
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
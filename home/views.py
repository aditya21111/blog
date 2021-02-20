from django.shortcuts import render,HttpResponse,redirect
from .models import Contact, userprofile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login as user_login ,logout as logout_user


from blog.models import Blogpost 


# Create your views here.
def home(request):
    return render(request,"home/index.html")
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        desc=request.POST.get('desc','')
        phone=request.POST.get('phone','')

        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        contacted=True
        return render(request,"home/contact.html",{"contacted":contacted,"name":name})
    return render(request,"home/contact.html")

def search(request):
    
    query=request.GET['query']
    if len(query)  > 80:
        posts = Blogpost.objects.none()
        messages.error(request, f'You have reached the word limit (80) of search')
    else:
        titlesearch=Blogpost.objects.filter(title__icontains=query)
        contentsearch=Blogpost.objects.filter(para1__icontains=query)
        authorsearch=Blogpost.objects.filter(writer__icontains=query)
        posts=titlesearch.union(contentsearch,authorsearch)

        # union -for merging query sets

    if posts.count() == 0:
        messages.error(request, 'Please use suitable keywords')

    params={"search":posts,'query':query}
    
    return render(request,"home/search.html",params)

    

def about(request):
    return HttpResponse("about page")




# creating users
def signup(request):

    if request.method=="POST":
        username=request.POST['username']
        firstname=request.POST['name1']
        lastname=request.POST['name2']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        if len(username)>10:
            messages.error(request,"username must be less than 10 characters")
            return redirect("/blog")
        if len(pass1)<4:
            messages.error(request,"Enter a strong password")
        if pass1!=pass2:
            messages.error(request,"Passwords must  match")
            return redirect("/blog")

        if not username.isalnum():
            messages.error( request,"Username must contain letter and numbers")

        else:
            users=User.objects.create_user(username,email,pass1)
            users.first_name= firstname
            users.last_name= lastname
            users.save()
            return redirect("/blog")
        


    else:
        return HttpResponse("404")
    





def login(request):
    if request.method=="POST":
        usernamelogin=request.POST['loginusername'] 
        loginpass=request.POST["loginpass"]
        users=authenticate(username=usernamelogin,password=loginpass)
        print(users)
        
        #authenticate returns none when credentials are wrong

        if users is not None:
            user_login(request,users)
            messages.success(request,"successfully loged inn")
            return redirect("/blog")

        else:
            messages.error(request,"invalid credentials")
            return redirect("/blog")
       

    else:
        return HttpResponse("404")


def logout(request):
    logout_user(request)
    messages.success(request,"successfully loged out !")
    return redirect("/blog")


def profile(request):
    
    if request.method=="POST":
        try:
            userimg=request.FILES['userimg']
        except Exception as e:
            pass
            count=userprofile.objects.count()
            userimages=userprofile.objects.filter(user=request.user,sno=count)
            for i in userimages:
                userimg=i.pic
                print(userimg)
        tel=request.POST.get('tel','')
        country=request.POST.get('country',"")
        state=request.POST.get('state',"")
        user=request.user
                
        profile=userprofile(pic=userimg,tel=tel,state=state,country=country,user=user)
                
        profile.save()
        messages.success(request,'profile updated successfully 😃')   
            
        return redirect("/blog")
            
    
        
        try:
            userpic=userprofile.objects.filter(user=request.user).order_by("-updated_at").first()
            print(userpic)

        except Exception as e:
            messages.error( request,"profile not updated please try again")
            return redirect("/blog")
    
    

    
    
    
    
    
    
    return render(request,"home/profile.html",{"profile":userpic})

   
        
    

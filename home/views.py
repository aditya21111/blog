from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login as user_login ,logout as logout_user
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver


from django.contrib.auth.decorators import login_required


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
        
        try:
            subject, from_email, to = 'Thank you', 'writerhubhere@gmail.com', email
            text_content = ""
            html_content = f'Hey <strong>{name}</strong>\n Thank you for contacting us\n We have received your enquiry and will respond you within 24 hours. For urgent enquiries please call us on one of the number below\n +91 some number'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        except Exception as e:
            return HttpResponse(e)  
        # try:
        #     send_mail("Thank you 😊", f"Hey , {name} Thank you for contacting us\n We have received your enquiry and will respond you within 24 hours. For urgent enquiries please call us on one of the number below\n +91 some number ","writerhubhere@gmail.com", [email])
        # except Exception as e:
        #     return HttpResponse(e)
        return render(request,"home/contact.html",{"contacted":contacted,"name":name})
        
       
        
    
       
    return render(request,"home/contact.html")

def search(request):
    try:
        query=request.GET['query']
        if len(query)  > 80:
            posts = Blogpost.objects.none()
            messages.error(request, f'You have reached the word limit (80) of search')
        else:
            titlesearch=Blogpost.objects.filter(title__icontains=query)
            contentsearch=Blogpost.objects.filter(content__icontains=query)
            authorsearch=Blogpost.objects.filter(writer__icontains=query)
            posts=titlesearch.union(contentsearch,authorsearch)

            # union -for merging query sets

        if posts.count() == 0:
            messages.error(request, 'Please use suitable keywords')

        params={"search":posts,'query':query}
        
        return render(request,"home/search.html",params)
    except Exception as e:
        return HttpResponse(e)
    

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
        try:
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
        
        except Exception as e:
            print(e)
    else:
        return HttpResponse("go to /blog and login")


def logout(request):
    
    logout_user(request)
    messages.success(request,"successfully loged out !")
    return redirect("/blog")

#profile update/create
@login_required

def profile(request,  **kwargs):
  
    return render(request,"home/profile.html")



def policy(request):
    return render(request,"home/policy.html")
                

        
    

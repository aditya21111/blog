from django.shortcuts import render
from newsletter.models import Newsletter
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
# Create your views here.
def subscribe(request):
    if request.method=="POST":
        email=request.POST.get('subMail','')
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request,"Sorry this email is already subscribed .")
            return redirect('/blog')
        else:
            subscribe=Newsletter(email=email)
            subscribe.save()
            messages.success(request,"😀 Thanks for subscribing us. Now you will get all updated from Writer-hub ")
            try:
                subject, from_email, to = 'Thank you for subscribing us', settings.EMAIL_HOST_USER, email
                with open(str(settings.BASE_DIR)+"/templates/newsletter/subscribe_email.txt") as f:
                    text_content = f.read()
                t=get_template("newsletter/subscribe_email.html")
                html_content = t.render()        
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except Exception as e:
                print(e)  
            return redirect("/blog")
    else:
        return HttpResponse("<h1 style='text-align:center;'>404</h1><br><h2 style='text-align:center;'>Page not found</h2>")
        return redirect("/blog")


def unsubscribe(request):
    if request.method=="POST":
        email=request.POST.get('unsubMail','')
        if Newsletter.objects.filter(email=email).exists():
            Newsletter.objects.filter(email=email).delete()
            messages.success(request,"You have been unsubscribed ☹")
            try:
                subject, from_email, to = 'unsubscribe notifcaation', 'writerhubhere@gmail.com', email
                with open(setting.BASE_DIR+"/templates/newsletter/unsub_email.txt") as f:
                    text_content = f.read()
                t=get_template("newsletter/unsub_email.html")
                html_content = t.render()        
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

            except Exception as e:
                print(e)
            return redirect("/blog")

        else:
            messages.error(request,"Sorry this email doesn't exsist. please recheck and proceed.")
            return redirect("/blog")

    else:
        return render(request,"newsletter/unsub.html")


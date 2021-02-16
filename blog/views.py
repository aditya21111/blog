from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User


from blog.models import Blogpost,comments
from home.models import userprofile

# Create your views here.
def blogHome(request):
    blog=Blogpost.objects.all().order_by("-pub_date")

    

    return render(request,"blog/blog.html",{"blog":blog})

def blogPost(request,slug):
  
    
    post=Blogpost.objects.filter(slug=slug)[0]
    otherPosts=Blogpost.objects.exclude(slug=slug)
    comment=comments.objects.filter(post=post)
    if  request.user.is_authenticated:
        profile=userprofile.objects.filter(user=request.user)
        return render(request,"blog/blogpost.html",{"post":post,"others":otherPosts,"comment":comment,"profile":profile})
    return render(request,"blog/blogpost.html",{"post":post,"others":otherPosts,"comment":comment})
def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postsno=request.POST.get("sno")
        post=Blogpost.objects.get(post_id=postsno)
    
        comment=comments(comment=comment,user=user,post=post)
        
        comment.save()
        messages.success(request,"comment posted successfully")
        return redirect(f"/blog/{post.slug}")

    return HttpResponse("byee")
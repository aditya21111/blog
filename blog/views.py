from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import Blogpost,comments


# Create your views here.
def blogHome(request):
    blog=Blogpost.objects.all().order_by("-pub_date")
    page = request.GET.get('page', 1)
    
    paginator = Paginator(blog, 12)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)


    return render(request,"blog/blog.html",{"blog":blog})

def blogPost(request,slug):
  
    try:
        post=Blogpost.objects.filter(slug=slug)[0]
        
        otherPosts=Blogpost.objects.exclude(slug=slug)
        comment=comments.objects.filter(post=post).order_by("-timestamp") 

        
        if  request.user.is_authenticated:
            
            return render(request,"blog/blogpost.html",{"post":post,"others":otherPosts,"comment":comment})
        return render(request,"blog/blogpost.html",{"post":post,"others":otherPosts,"comment":comment})

    except Exception as e:
        return HttpResponse(e )
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
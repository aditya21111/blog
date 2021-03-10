from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.templatetags import extras
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
        comment=comments.objects.filter(post=post,parent=None,is_approved=True).order_by("-timestamp") 
        replies=comments.objects.filter(post=post,is_approved=True).exclude(parent=None).order_by("-timestamp")
        
        replyDict={}
        for reply in replies:
            
            if reply.parent.sno not in replyDict.keys():
                replyDict[reply.parent.sno]=[reply]
            else:
                replyDict[reply.parent.sno].append(reply)

        if  request.user.is_authenticated:
            
            return render(request,"blog/blogpost.html",{"post":post,"others":otherPosts,"comment":comment,'replyDict': replyDict})
        return render(request,"blog/blogpost.html",{"post":post,"others":otherPosts,"comment":comment})

    except Exception as e:
        return HttpResponse(e )
def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postsno=request.POST.get("sno")
        post=Blogpost.objects.get(post_id=postsno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=comments(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully. it will be displayed after checked by our team.")
        else:
            parent= comments.objects.get(sno=parentSno)
            comment=comments(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request,"reply posted successfully.It will be displayed after checked by our team.")
        
        
        
        return redirect(f"/blog/{post.slug}")

    return HttpResponse("byee")
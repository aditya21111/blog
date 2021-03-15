from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.templatetags import extras
from blog.models import Blogpost,comments
from taggit.models import Tag
from django.db.models import Count

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

def blogPost(request,slug,tag_slug=None):
  
    try:
        
        tag=None
        if tag_slug:
            tag=get_object_or_404(Tag,slug=tag_slug)
           
        tag_slug=Blogpost.tags.values_list('id',flat=True)
        Similarpost=Blogpost.objects.filter(tags__in=tag_slug).exclude(slug=Blogpost.post_id)
        Similarpost=Similarpost.annotate(same_tags=Count('tags')).order_by('-same_tags','-pub_date')
        print(Similarpost)
        post=Blogpost.objects.filter(slug=slug)[0]
        

        comment=comments.objects.filter(post=post,parent=None,is_approved=True).order_by("-timestamp") 
        replies=comments.objects.filter(post=post,is_approved=True).exclude(parent=None).order_by("-timestamp")
        
        replyDict={}
        for reply in replies:
            
            if reply.parent.sno not in replyDict.keys():
                replyDict[reply.parent.sno]=[reply]
            else:
                replyDict[reply.parent.sno].append(reply)

        if  request.user.is_authenticated:
            
            return render(request,"blog/blogpost.html",{"post":post,"comment":comment,'replyDict': replyDict,"tag":tag,'similar':Similarpost})
        return render(request,"blog/blogpost.html",{"post":post,"comment":comment,"tag":tag,'similar':Similarpost})

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

def tagfilter(request,tag):
    if get_object_or_404(Tag,slug=tag) is not None:
    
        tagg=get_object_or_404(Tag,slug=tag)
        post_to_tag=Blogpost.objects.filter(tags__name__in=[tagg])
        
        print(Blogpost.tags.most_common()[:10])
        common_tags=Blogpost.tags.most_common()[:10]
        
        return render(request,"blog/tag_filter.html",{'post_to_tag':post_to_tag,"tag":tag,"common_tags":common_tags})
    else:
        return HttpResponse("No such tag exsist")

    return HttpResponse("hello")


    
    
   
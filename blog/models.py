from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from home.models import userprofile
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE

# Create your models here.
class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100, default="")
    pub_date=models.DateTimeField(default=now)
    writer=models.CharField(max_length=60,default="")
    thumbnail=models.ImageField(upload_to="blog/images" , default="")
  
    content = HTMLField()
    
 
    category=models.CharField(max_length=15,default="")
   
    thumbnail=models.ImageField(upload_to="media/blog/images" , default="")
    slug=models.CharField(default="", max_length=50)

    def __str__(self):
        return self.title

class comments(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
   
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    post=models.ForeignKey(Blogpost,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,default=None)
    timestamp=models.DateTimeField( auto_now=False, auto_now_add=False ,default=now)

    def __str__(self):
        return self.comment[0:14] + ".....  " + "by " + self.user.username
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from home.models import userprofile



# Create your models here.
class Blogpost(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100, default="")
    pub_date=models.DateTimeField(default=now)
    writer=models.CharField(max_length=60,default="")
    thumbnail=models.ImageField(upload_to="blog/images" , default="")
    postimgdesc=models.CharField(max_length=200,default="")
    para1=models.CharField (max_length=3000, default='')

    head0=models.CharField(max_length=150, default='',blank=True)
    head0para=models.CharField(max_length=4000 ,default='')
    category=models.CharField(max_length=15,default="")
    head1=models.CharField(max_length=150,default="",blank=True)
    head1para=models.CharField(max_length=2000,default="",blank=True)
    head2=models.CharField(max_length=150,default="",blank=True)
    head2para=models.CharField(max_length=2000,default="",blank=True)
    
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
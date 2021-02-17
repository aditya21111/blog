from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=300)
    
  
    phone=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=300,default="")
 
    

    def __str__(self):
        return self.name

class userprofile(models.Model):
    pic=models.ImageField(blank=True,null=True,upload_to="media",default=None)
    sno=models.AutoField(blank=True,primary_key=True,unique=True,default=None)
    tel=models.CharField(default="1",null=True,max_length=12)
    country=models.CharField(max_length=50,default='',null=True)
    state=models.CharField(max_length=50,default='',null=True)
    updated_at=models.DateTimeField(null=True,default=now)
    
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.user.get_username()
  
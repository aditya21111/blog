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


class Profile(models.Model):
    user=models.OneToOneField(User,blank=True, on_delete=models.CASCADE)
    pic=models.ImageField( upload_to="media/profiles",blank=True)

    def __str__(self):
        return str(self.user) + " updated his profile."
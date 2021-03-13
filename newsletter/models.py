from django.db import models
from django.utils.timezone import now
# Create your models here.
class Newsletter(models.Model):
    email=models.EmailField( max_length=60 , unique=True)
    subscribed_at=models.DateTimeField( auto_now=False, auto_now_add=False,null=True,default=now)


    def __str__(self):
        return self.email
    
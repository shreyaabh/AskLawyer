from django.db import models
from api.models import askLawyer
from django.contrib.auth.models import User


# Create your models here.
class forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    
    topic= models.CharField(max_length=100)
    description = models.TextField()
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.topic)
 

class Discussion(models.Model):
    user = models.ForeignKey(askLawyer, on_delete=models.CASCADE)
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    discuss = models.TextField()
 
    def __str__(self):
        return str(self.forum)


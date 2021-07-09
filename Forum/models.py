from django.db import models
from api.models import askLawyer


# Create your models here.
class forum(models.Model):
    full_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200,null=True)
    topic= models.CharField(max_length=100)
    description = models.TextField()
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.full_name)
 

class Discussion(models.Model):
    user = models.ForeignKey(askLawyer, on_delete=models.CASCADE)
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    discuss = models.TextField()
 
    def __str__(self):
        return str(self.forum)


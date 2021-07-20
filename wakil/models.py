from django.db import models
from django.contrib.auth.models import User
from api.models import answer
# Create your models here.
class Profile(models.Model):
    CHOICES=[
        ('approved','approved'),
        ('rejected','rejected'),
    ]
    s_no=models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    biography=models.TextField(blank=False)
    award=models.TextField(blank=False)
    practice_area=models.CharField(max_length=30)
    experience= models.FloatField(blank=True)
    legal_fees= models.IntegerField(default=15, blank=True)
    publication=models.TextField(blank=False)
    website=models.URLField(max_length=200)
    status=models.CharField(choices=CHOICES,max_length=20)
    professional_associations=models.CharField(max_length=200)
    image=models.ImageField(upload_to='profile/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.award
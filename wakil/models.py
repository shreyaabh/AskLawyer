from django.db import models
from django.contrib.auth.models import User
from api.models import answer
# Create your models here.

class Education(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    degree=models.CharField(max_length=30)
    university=models.CharField(max_length=30)
    faculty=models.CharField(max_length=30)
    institute=models.CharField(max_length=30)
    year = models.DateField()

    def __str__(self):
        return self.degree

class Experience(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    organization=models.CharField(max_length=30,blank=False)
    position=models.CharField(max_length=30,blank=False)
    description=models.TextField(blank=True)
    institute=models.CharField(max_length=30)
    date_from = models.DateField(blank=False)
    date_to = models.DateField()

    def __str__(self):
        return self.organization

class Awards(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    award_title=models.CharField(max_length=30,blank=False)
    awarded_by=models.CharField(max_length=30,blank=False)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.award_title

class Link(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    facebook=models.URLField(max_length=200)
    instagram=models.URLField(max_length=200)
    linkedin=models.URLField(max_length=200)
    twitter=models.URLField(max_length=200)
    youtube=models.URLField(max_length=200)

    def __str__(self):
        return self.facebook

class Profile(models.Model):
    CHOICES=[
        ('approved','approved'),
        ('rejected','rejected'),
    ]
    s_no=models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    biography=models.TextField(blank=False)
    award=models.ForeignKey(Awards, on_delete=models.CASCADE)
    practice_area=models.CharField(max_length=30)
    experience=models.ForeignKey(Experience, on_delete=models.CASCADE)
    legal_fees= models.IntegerField(default=15, blank=True)
    publication=models.TextField(blank=False)
    links=models.ForeignKey(Link, on_delete=models.CASCADE)
    status=models.CharField(choices=CHOICES,max_length=20)
    professional_associations=models.CharField(max_length=200)
    image=models.ImageField(upload_to='profile/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user



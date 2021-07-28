from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

# Create your views here.
class profileModelViewset(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer

class educationModelViewset(viewsets.ModelViewSet):
    queryset=Education.objects.all()
    serializer_class=EducationSerializer

class experienceModelViewset(viewsets.ModelViewSet):
    queryset=Experience.objects.all()
    serializer_class=ExperienceSerializer

class awardsModelViewset(viewsets.ModelViewSet):
    queryset=Awards.objects.all()
    serializer_class=AwardsSerializer

class linkModelViewset(viewsets.ModelViewSet):
    queryset=Link.objects.all()
    serializer_class=LinkSerializer

    


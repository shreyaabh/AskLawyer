from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

# Create your views here.
class askUserModelViewset(viewsets.ModelViewSet):
    queryset=askUser.objects.all()
    serializer_class=askUserSerializer

class questionModelViewset(viewsets.ModelViewSet):
    queryset=question.objects.all()
    serializer_class=questionSerializer

class askLawyerModelViewset(viewsets.ModelViewSet):
    queryset=askLawyer.objects.all()
    serializer_class=askLawyerSerializer

class answerModelViewset(viewsets.ModelViewSet):
    queryset=answer.objects.all()
    serializer_class=answerSerializer 

class pointsAllocateModelViewset(viewsets.ModelViewSet):
    queryset=PointsAllocated.objects.all()
    serializer_class=pointsAllocateSerializer
    
class pointsModelViewset(viewsets.ModelViewSet):
    queryset=Points.objects.all()
    serializer_class=pointsSerializer


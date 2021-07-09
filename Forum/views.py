from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

# Create your views here.
class forumModelViewset(viewsets.ModelViewSet):
    queryset=forum.objects.all()
    serializer_class=forumSerializer

class DiscussionModelViewset(viewsets.ModelViewSet):
    queryset=Discussion.objects.all()
    serializer_class=DiscussionSerializer
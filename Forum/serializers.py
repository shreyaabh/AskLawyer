from django.db.models import fields
from rest_framework import serializers
from .models import *

class forumSerializer(serializers.ModelSerializer):
    class Meta:
        model=forum
        fields='__all__'
        
class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Discussion
        fields='__all__'

    
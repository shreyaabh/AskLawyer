from django.db.models import fields
from rest_framework import serializers
from .models import *

class askUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=askUser
        fields='__all__'
        
class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model=question
        fields='__all__'

class askLawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model=askLawyer
        fields='__all__'

class answerSerializer(serializers.ModelSerializer):
    question=serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model=answer
        fields='__all__'    
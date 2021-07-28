from django.db.models import fields
from rest_framework import serializers
from .models import *

class pointsAllocateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Points
        fields='__all__'

class pointsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Points
        fields=('user','stars',)

class askUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=askUser
        fields='__all__'
        
class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model=question
        fields='__all__'

class askLawyerSerializer(serializers.ModelSerializer):
    points=pointsSerializer(many=True, read_only=True)
    class Meta:
        model=askLawyer
        fields=('id',
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "address","points",'total_points','no_rating')

class answerSerializer(serializers.ModelSerializer):
    #question=serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model=answer
        fields=('user','question','answer','correct','correct')



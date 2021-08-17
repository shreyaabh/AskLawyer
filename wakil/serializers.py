from django.db.models import fields
from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'
        
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields='__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experience
        fields='__all__'

class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Awards
        fields='__all__'

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Link
        fields='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'
    
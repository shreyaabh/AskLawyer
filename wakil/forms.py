from django.db.models import fields
from django.forms.models import inlineformset_factory
from .models import *

ProfileFormset=inlineformset_factory(Profile,Education,fields=('user',))
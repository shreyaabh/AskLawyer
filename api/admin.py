from django.contrib import admin
from .models import question,askUser,answer,askLawyer

# Register your models here.
admin.site.register(askUser)
admin.site.register(question)
admin.site.register(askLawyer)
admin.site.register(answer)

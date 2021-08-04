from django.contrib import admin
from .models import Profile,Education,Experience,Awards,Link

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    fieldsets=(
        ('Profile',
        {
            'fields':('user','biography','practice_area','legal_fees','status','professional_associations','image','publication',),
        }),
        ('Experience',
        {
            'fields':('experience',),
        }),
        ('Awards',
        {
            'fields':('award',),
        }),
        ('Links',
        {
            'fields':('links',),
        }),
    )

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Awards)
admin.site.register(Link)

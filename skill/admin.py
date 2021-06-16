from django.contrib import admin

from .models import *

class SkillAdmin(admin.ModelAdmin):

    list_filter = ('tree',)
    class Meta:
        model = Skill

admin.site.register(Weapon)
admin.site.register(Skill,SkillAdmin)
admin.site.register(SkillTree)
admin.site.register(Build)


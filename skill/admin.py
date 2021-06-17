from django.contrib import admin

from .models import *

class SkillAdmin(admin.ModelAdmin):

    list_filter = ('tree',)
    class Meta:
        model = Skill

class BuildAdmin(admin.ModelAdmin):
    list_display = ['name','is_active']
    list_filter = ('is_active',)
    class Meta:
        model = Build

admin.site.register(Weapon)
admin.site.register(Skill,SkillAdmin)
admin.site.register(SkillTree)
admin.site.register(Build,BuildAdmin)


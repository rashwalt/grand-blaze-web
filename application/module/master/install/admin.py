# -*- coding: utf-8 -*-

from django.contrib import admin
from module.master.install import models

class InstallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
class InstallSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'install', 'level')

admin.site.register(models.Install, InstallAdmin)
admin.site.register(models.InstallSkill, InstallSkillAdmin)

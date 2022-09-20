# -*- coding: utf-8 -*-

from django.contrib import admin
from module.master.skill import models

class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sk_comment')

class SkillGetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'skill_id')

class SkillGetListAdmin(admin.ModelAdmin):
    list_display = ('id', 'tm_level', 'tm_race', 'skill', 'skill_name', 'skill_comment', 'condition_text')

class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(models.Skill, SkillAdmin)
admin.site.register(models.SkillGet, SkillGetAdmin)
admin.site.register(models.SkillGetList, SkillGetListAdmin)
admin.site.register(models.SkillCategory, SkillCategoryAdmin)

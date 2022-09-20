# -*- coding: utf-8 -*-

from django.contrib import admin
from module.character import models

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('user', 'character_name')

class CharacterBattleAdmin(admin.ModelAdmin):
    list_display = ('user', 'level')

class CharacterActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_no')

class CharacterKeyItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'keyitem_id')

class CharacterHavingSkillAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill_id')

class CharacterHavingItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'have_no')

class CharacterQuestAdmin(admin.ModelAdmin):
    list_display = ('user', 'quest_id', 'clear_fg', 'step')

class CharacterInstallAdmin(admin.ModelAdmin):
    list_display = ('user', 'install_id', 'level')

class CharacterMovingMarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'mark_id')

admin.site.register(models.Character, CharacterAdmin)
admin.site.register(models.CharacterBattle, CharacterBattleAdmin)
admin.site.register(models.CharacterAction, CharacterActionAdmin)
admin.site.register(models.CharacterKeyItem, CharacterKeyItemAdmin)
admin.site.register(models.CharacterHavingSkill, CharacterHavingSkillAdmin)
admin.site.register(models.CharacterHavingItem, CharacterHavingItemAdmin)
admin.site.register(models.CharacterQuest, CharacterQuestAdmin)
admin.site.register(models.CharacterInstall, CharacterInstallAdmin)
admin.site.register(models.CharacterMovingMark, CharacterMovingMarkAdmin)

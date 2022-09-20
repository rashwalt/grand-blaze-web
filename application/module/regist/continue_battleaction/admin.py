# -*- coding: utf-8 -*-

from django.contrib import admin
from module.regist.continue_battleaction import models

class ContinueBattleActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'action_no', 'created_at', 'updated_at')

class SavingActionHeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')

class SavingActionBodyAdmin(admin.ModelAdmin):
    list_display = ('id', 'saving_action', 'action_no', 'created_at', 'updated_at')

admin.site.register(models.ContinueBattleAction, ContinueBattleActionAdmin)
admin.site.register(models.SavingActionHead, SavingActionHeadAdmin)
admin.site.register(models.SavingActionBody, SavingActionBodyAdmin)

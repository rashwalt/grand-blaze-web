# -*- coding: utf-8 -*-

from django.contrib import admin
from module.master.battleaction import models

class BattleActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment')
    
class BattleTargetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'comment', 'view_no', 'target_type', 'target_no')

admin.site.register(models.BattleAction, BattleActionAdmin)
admin.site.register(models.BattleTarget, BattleTargetAdmin)

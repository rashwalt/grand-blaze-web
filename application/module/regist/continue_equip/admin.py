# -*- coding: utf-8 -*-

from django.contrib import admin
from module.regist.continue_equip import models

class ContinueEquipAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')

admin.site.register(models.ContinueEquip, ContinueEquipAdmin)

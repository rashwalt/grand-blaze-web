# -*- coding: utf-8 -*-

from django.contrib import admin
from module.regist.continue_main import models

class ContinueMainAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')

admin.site.register(models.ContinueMain, ContinueMainAdmin)

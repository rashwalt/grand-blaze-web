# -*- coding: utf-8 -*-

from django.contrib import admin
from module.regist.continue_complete import models

class ContinueCompleteAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'created_at', 'updated_at')

admin.site.register(models.ContinueComplete, ContinueCompleteAdmin)

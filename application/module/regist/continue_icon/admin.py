# -*- coding: utf-8 -*-

from django.contrib import admin
from module.regist.continue_icon import models

class ContinueIconAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'icon_id', 'created_at', 'updated_at')

admin.site.register(models.ContinueIcon, ContinueIconAdmin)

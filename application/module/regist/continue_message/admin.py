# -*- coding: utf-8 -*-

from django.contrib import admin
from module.regist.continue_message import models

class ContinueMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'mes_no', 'created_at', 'updated_at')

admin.site.register(models.ContinueMessage, ContinueMessageAdmin)

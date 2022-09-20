# -*- coding: utf-8 -*-

from django.contrib import admin
from module.master.management import models

class ManagementAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_regist_stop')

admin.site.register(models.Management, ManagementAdmin)
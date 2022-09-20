# -*- coding: utf-8 -*-

from django.contrib import admin
from module.regist.continue_profile import models

class ContinueProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')

admin.site.register(models.ContinueProfile, ContinueProfileAdmin)

# -*- coding: utf-8 -*-

from django.contrib import admin
from module.regist.continue_serif import models

class ContinueSerifAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'word_no', 'created_at', 'updated_at')

class SavingSerifHeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')

class SavingSerifBodyAdmin(admin.ModelAdmin):
    list_display = ('id', 'saving_action', 'word_no', 'created_at', 'updated_at')

admin.site.register(models.ContinueSerif, ContinueSerifAdmin)
admin.site.register(models.SavingSerifHead, SavingSerifHeadAdmin)
admin.site.register(models.SavingSerifBody, SavingSerifBodyAdmin)

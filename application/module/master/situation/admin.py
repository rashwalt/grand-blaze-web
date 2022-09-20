# -*- coding: utf-8 -*-

from django.contrib import admin
from module.master.situation import models

class SituationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(models.Situation, SituationAdmin)

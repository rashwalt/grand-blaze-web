# -*- coding: utf-8 -*-

from django.contrib import admin
from module.master.race import models

class RaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(models.Race, RaceAdmin)

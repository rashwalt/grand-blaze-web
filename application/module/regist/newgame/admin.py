# -*- coding: utf-8 -*-

from django.contrib import admin
from module.regist.newgame import models

class NewGameAdmin(admin.ModelAdmin):
    list_display = ('user', 'character_name','created_at', 'updated_at')

admin.site.register(models.NewGame, NewGameAdmin)

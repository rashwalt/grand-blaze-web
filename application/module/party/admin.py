# -*- coding: utf-8 -*-

from django.contrib import admin
from module.party import models

class PartyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class PartyBelongAdmin(admin.ModelAdmin):
    list_display = ('user', 'party')

admin.site.register(models.Party, PartyAdmin)
admin.site.register(models.PartyBelong, PartyBelongAdmin)

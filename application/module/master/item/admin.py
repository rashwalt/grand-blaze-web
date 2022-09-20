# -*- coding: utf-8 -*-

from django.contrib import admin
from module.master.item import models

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.ItemType, ItemTypeAdmin)

# -*- coding: utf-8 -*-

from django.contrib import admin
from module.link import models

class LinkCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
class LinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'comment', 'category', 'owner', 'url')

admin.site.register(models.LinkCategory, LinkCategoryAdmin)
admin.site.register(models.Link, LinkAdmin)

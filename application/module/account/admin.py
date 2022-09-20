# -*- coding: utf-8 -*-

from django.contrib import admin
from module.account import models

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_name', 'official_news', 'created_at', 'updated_at')
    
class InstantMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'from_user', 'title', 'read_complete', 'created_at', 'updated_at')

admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.InstantMessage, InstantMessageAdmin)

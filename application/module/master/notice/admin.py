# -*- coding: utf-8 -*-

from django.contrib import admin
from module.master.notice import models

class NoticeAdmin(admin.ModelAdmin):
    date_hierarchy = 'view_date'
    list_display = ('id', 'is_valid', 'title', 'body', 'category', 'rank', 'view_date', 'limit_date', 'created_at', 'updated_at')

admin.site.register(models.Notice, NoticeAdmin)

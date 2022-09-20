# -*- coding: utf-8 -*-

from django.contrib import admin
from module.forum import models

class ForumAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_forum', 'is_not_auth')
    
class ForumStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'forum', 'name', 'is_staff_only', 'is_new_thread', 'is_thread_rock')
    
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'forum', 'title', 'create_user', 'view_count', 'is_rock', 'thread_solid', 'forum_status', 'created_at', 'updated_at')
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'thread', 'body', 'user', 'is_delete', 'delete_user', 'delete_mean', 'created_at', 'updated_at')

admin.site.register(models.Forum, ForumAdmin)
admin.site.register(models.ForumStatus, ForumStatusAdmin)
admin.site.register(models.Thread, ThreadAdmin)
admin.site.register(models.Article, ArticleAdmin)

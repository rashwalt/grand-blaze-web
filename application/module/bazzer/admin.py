# -*- coding: utf-8 -*-

from django.contrib import admin
from module.bazzer import models
    
class BazzerAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'seller', 'price', 'seller_date', 'status', 'created_at', 'updated_at')

admin.site.register(models.Bazzer, BazzerAdmin)
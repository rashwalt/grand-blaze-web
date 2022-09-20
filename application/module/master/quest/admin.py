# -*- coding: utf-8 -*-

from django.contrib import admin
from module.master.quest import models

class QuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class FieldTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class WeatherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MarkWeatherAdmin(admin.ModelAdmin):
    list_display = ('id', 'mark', 'count', 'weather')

admin.site.register(models.Quest, QuestAdmin)
admin.site.register(models.Mark, MarkAdmin)
admin.site.register(models.FieldType, FieldTypeAdmin)
admin.site.register(models.Weather, WeatherAdmin)
admin.site.register(models.MarkWeather, MarkWeatherAdmin)

# -*- coding: utf-8 -*-

from django.contrib import admin
from module.regist.continue_trade import models

class ContinueShoppingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'shop_act', 'shopping_no', 'created_at', 'updated_at')

class ContinueTradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'trade_no', 'trade_item_no', 'created_at', 'updated_at')

admin.site.register(models.ContinueShopping, ContinueShoppingAdmin)
admin.site.register(models.ContinueTrade, ContinueTradeAdmin)

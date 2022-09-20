# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import MultiRegistCachedModel

from module.master.item.models import Item

from module.regist.constant import RegistConstant
from module.character.models import Character, CharacterHavingItem

class ContinueShopping(MultiRegistCachedModel):
    """
    売買登録
    """
    shop_act = models.IntegerField(u'ショップ種別', choices=RegistConstant.SHOP_ACTS, null=True, blank=True)
    shopping_no = models.IntegerField(u'ショッピング番号', null=True, blank=True)
    item_no = models.IntegerField(u'アイテムID', null=True, blank=True)
    item_count = models.IntegerField(u'アイテム個数', null=True, blank=True)

    class Meta:
        verbose_name = u'売買登録'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s-%s-%s: ContinueShopping' % (self.user_id, self.shop_act, self.shopping_no)

    def save(self, *args, **kwargs):
        super(ContinueShopping, self).save(*args, **kwargs)
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))

    def delete(self, *args, **kwargs):
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))
        super(ContinueShopping, self).delete(*args, **kwargs)
    
    @property
    def item(self):
        return Item.get(self.item_no)
    
    @property
    def having_item(self):
        return CharacterHavingItem.get_chara_item(self.user, self.item_no)

class ContinueTrade(MultiRegistCachedModel):
    """
    取引登録
    """
    trade_no = models.IntegerField(u'取引番号', null=True, blank=True)
    trade_entry = models.IntegerField(u'取引相手No', null=True, blank=True)
    trade_item_no = models.IntegerField(u'取引アイテムID', null=True, blank=True)
    trade_number = models.IntegerField(u'取引個数', null=True, blank=True)
    trade_message = models.CharField(u'取引メッセージ', max_length=200, blank=True)
    trade_speed = models.BooleanField(u'速達で送る', default=False, blank=True)

    class Meta:
        verbose_name = u'取引登録'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s-%s: ContinueTrade' % (self.user_id, self.trade_no)

    def save(self, *args, **kwargs):
        super(ContinueTrade, self).save(*args, **kwargs)
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))

    def delete(self, *args, **kwargs):
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))
        super(ContinueTrade, self).delete(*args, **kwargs)
    
    @property
    def item(self):
        return Item.get(self.trade_item_no)
    
    @property
    def target(self):
        return Character.get(self.trade_entry)
    
    @property
    def having_item(self):
        return CharacterHavingItem.get_chara_item(self.user, self.trade_item_no)


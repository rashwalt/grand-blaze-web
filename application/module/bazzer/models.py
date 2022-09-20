# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import User

from module.abstract.cachedmodels.models import CachedModel

from module.master.item.models import Item
from module.account.api import UserProfileAPI

from module.bazzer.constant import BazzerConstant

class Bazzer(CachedModel):
    """
    バザー出品物リスト
    """
    
    item = models.ForeignKey(Item, verbose_name=u'アイテム',db_index=True)
    seller = models.ForeignKey(User, verbose_name=u'出品者', related_name='seller_users', db_index=True)
    seller_having_no = models.IntegerField(u'出品者所持番号', default=0)
    price = models.PositiveIntegerField(u'出品価格', default=1)
    seller_date = models.DateTimeField(u'出品時間', default=datetime.datetime.now())
    status = models.PositiveSmallIntegerField(u'状態', default=BazzerConstant.BAZZER_STATUS_SELL, choices=BazzerConstant.BAZZER_STATUSES)
    buyer = models.ForeignKey(User, verbose_name=u'落札者', related_name='buyer_users', default=None, blank=True, null=True)
    buyer_date = models.DateTimeField(u'取引確定時間', default=None, blank=True, null=True)
    done = models.BooleanField(u'取り込み済', default=False)

    class Meta:
        verbose_name = u'バザー出品物リスト'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  'Bazzer:%s' % self.id

    def save(self, *args, **kwargs):
        super(Bazzer, self).save(*args, **kwargs)
        cache.delete(self._get_get_item_history_list_cache_key(self.item_id))
        cache.delete(self._get_get_seller_history_list_cache_key(self.seller_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_item_history_list_cache_key(self.item_id))
        cache.delete(self._get_get_seller_history_list_cache_key(self.seller_id))
        super(Bazzer, self).delete(*args, **kwargs)

    def get_seller_name(self):
        if self.seller_id:
            return UserProfileAPI.get_user_name(self.seller)
        return ''

    def get_buyer_name(self):
        if self.buyer_id:
            return UserProfileAPI.get_user_name(self.buyer)
        return ''
    
    def get_item(self):
        return Item.get(self.item_id)

    @classmethod
    def _get_get_item_history_list_cache_key(cls, item_id):
        return '%s/get_item_history_list/%s' % (cls._meta, item_id)

    @classmethod
    def get_item_history_list(cls, item_id):
        cache_key = cls._get_get_item_history_list_cache_key(item_id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = list(cls.objects.filter(item=item_id, status=BazzerConstant.BAZZER_STATUS_COMPLETE))
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

    @classmethod
    def _get_get_seller_history_list_cache_key(cls, user_id):
        return '%s/get_seller_history_list/%s' % (cls._meta, user_id)

    @classmethod
    def get_seller_history_list(cls, user):
        cache_key = cls._get_get_item_history_list_cache_key(user.id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = list(cls.objects.filter(seller=user))
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

    @classmethod
    def get_search_article_list(cls, user, type, level, min_price, max_price, sort, is_mine, is_buy, limit=10):
        
        if is_buy:
            obj = cls.objects.filter(status=BazzerConstant.BAZZER_STATUS_COMPLETE, buyer=user)
        else:
            obj = cls.objects.filter(status=BazzerConstant.BAZZER_STATUS_SELL)
        
        if type > 0:
            obj = obj.filter(item__it_type=type)
        
        if level and level > 0:
            obj = obj.filter(item__it_equip_level__gte=level)
        
        if min_price and max_price and min_price > 0 and max_price > 0 and max_price >= min_price:
            obj = obj.filter(price__gte=min_price, price__lte=max_price)
        
        if is_mine:
            obj = obj.filter(seller=user)
            
        l = []

        if sort == BazzerConstant.SORT_NAME:
            l = list(obj.order_by('item__name'))
        elif sort == BazzerConstant.SORT_PRICE:
            l = list(obj.order_by('price'))
        elif sort == BazzerConstant.SORT_PHYSICAL:
            l = list(obj.order_by('item__it_physics'))
        elif sort == BazzerConstant.SORT_MAGICAL:
            l = list(obj.order_by('item__it_sorcery'))
        elif sort == BazzerConstant.SORT_PHYSICAL_PARRY:
            l = list(obj.order_by('item__it_physics_parry'))
        elif sort == BazzerConstant.SORT_MAGICAL_PARRY:
            l = list(obj.order_by('item__it_sorcery_parry'))
        else:
            l = list(obj.order_by('id'))

        return l
    
    @classmethod
    def create(cls, user, item, having_no, price):
        bazzer_data = cls.objects.create(item=item, seller=user, seller_having_no=having_no, price=price)
        
        return bazzer_data.id, None
    
    @classmethod
    def buy(cls, user, bazzer_id):
        bazzer_data = cls.objects.select_for_update().get(id=bazzer_id)
        
        if bazzer_data.status != BazzerConstant.BAZZER_STATUS_SELL:
            return False
        
        bazzer_data.status = BazzerConstant.BAZZER_STATUS_COMPLETE
        bazzer_data.buyer = user
        bazzer_data.buyer_date = datetime.datetime.now()
        bazzer_data.save()
        
        return True
    
    @classmethod
    def cancel(cls, user, bazzer_id):
        bazzer_data = cls.objects.select_for_update().get(id=bazzer_id)
        
        if bazzer_data.status != BazzerConstant.BAZZER_STATUS_SELL or bazzer_data.seller_id != user.id:
            return False
        
        bazzer_data.status = BazzerConstant.BAZZER_STATUS_CANCEL
        bazzer_data.save()
        
        return True


        
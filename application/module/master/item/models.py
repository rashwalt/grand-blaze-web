# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import CachedBaseModel

class Item(CachedBaseModel):
    name = models.CharField(u'名称', max_length=100)
    it_physics = models.IntegerField(u'物理攻撃', default=0)
    it_sorcery = models.IntegerField(u'魔法攻撃', default=0)
    it_physics_parry = models.IntegerField(u'物理回避', default=0)
    it_sorcery_parry = models.IntegerField(u'魔法回避', default=0)
    it_critical = models.IntegerField(u'クリティカル率', default=0)
    it_metal = models.IntegerField(u'金属度', default=0)
    it_charge = models.IntegerField(u'ウェイトタイム', default=0)
    it_range = models.IntegerField(u'射程', default=0)
    it_type = models.IntegerField(u'種類', default=0)
    it_sub_category = models.IntegerField(u'サブカテゴリ', default=0)
    it_attack_type = models.IntegerField(u'攻撃種別', default=0)
    it_comment = models.TextField(u'解説文', blank=True)
    it_fire = models.IntegerField(u'火', default=0)
    it_freeze = models.IntegerField(u'氷', default=0)
    it_air = models.IntegerField(u'風', default=0)
    it_earth = models.IntegerField(u'土', default=0)
    it_water = models.IntegerField(u'水', default=0)
    it_thunder = models.IntegerField(u'雷', default=0)
    it_holy = models.IntegerField(u'光', default=0)
    it_dark = models.IntegerField(u'闇', default=0)
    it_slash = models.IntegerField(u'斬', default=0)
    it_pierce = models.IntegerField(u'突', default=0)
    it_strike = models.IntegerField(u'打', default=0)
    it_break = models.IntegerField(u'壊', default=0)
    it_ok_sex = models.IntegerField(u'性別限定', default=0)
    it_ok_race = models.IntegerField(u'種族限定', default=0)
    it_both_hand = models.BooleanField(u'両手持ち？', default=False)
    it_use_item = models.IntegerField(u'使用可否', default=0)
    it_equip_install = models.CharField(u'装備クラス', max_length=100, blank=True)
    it_equip_parts = models.BooleanField(u'装備部位', default=False)
    it_rare = models.BooleanField(u'レアアイテム？', default=False)
    it_bind = models.BooleanField(u'バインドアイテム？', default=False)
    it_quest = models.BooleanField(u'クエストアイテム？', default=False)
    it_shop = models.IntegerField(u'販売可否', default=0)
    it_equip_level = models.IntegerField(u'装備レベル', default=0)
    it_target_area = models.IntegerField(u'対象範囲', default=0)
    it_price = models.DecimalField(u'販売価格', max_digits=13, decimal_places=1, default=0)
    it_seller = models.DecimalField(u'売却価格', max_digits=13, decimal_places=1, default=0)
    it_stack = models.IntegerField(u'スタック', default=0)

    class Meta:
        verbose_name = u'アイテム'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)
        cache.delete(self._get_get_chices_list_cache_key(self.it_type))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_chices_list_cache_key(self.it_type))
        super(Item, self).delete(*args, **kwargs)
    
    @property
    def item_type(self):
        return ItemType.get(self.it_type)

    @classmethod
    def _get_get_chices_list_cache_key(cls, category_id):
        return '%s/get_chices_list/%s' % (cls._meta, category_id)

    @classmethod
    def get_chices_list(cls, category_id):
        cache_key =  cls._get_get_chices_list_cache_key(category_id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(it_type=category_id, it_shop=1).order_by('id').values('id','name','it_price','it_comment')
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class ItemType(CachedBaseModel):
    name = models.CharField(u'名称', max_length=100)
    skill_id = models.IntegerField(u'テック', default=0)
    categ_div = models.IntegerField(u'カテゴリ', default=0)
    database_view = models.BooleanField(u'データ表示フラグ', default=True)
    
    it_stack = models.IntegerField(u'スタック', default=0)

    class Meta:
        verbose_name = u'アイテム種別'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(ItemType, self).save(*args, **kwargs)
        cache.delete(self._get_get_choice_list_cache_key())

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_choice_list_cache_key())
        super(ItemType, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_choice_list_cache_key(cls):
        return '%s/get_choice_list' % cls._meta

    @classmethod
    def get_choice_list(cls):
        cache_key = cls._get_get_choice_list_cache_key()

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = list(cls.objects.all().values_list('id', 'name'))
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l
        
        
        
        
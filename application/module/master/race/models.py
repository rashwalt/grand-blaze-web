# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import CachedBaseModel

from module.common.constant import CommonConstant

class Race(CachedBaseModel):
    name = models.CharField(u'名称', max_length=100)
    up_hp = models.IntegerField(u'HP成長ランク', choices=CommonConstant.GROWUPS, default=CommonConstant.GROWUP_G)
    up_mp = models.IntegerField(u'MP成長ランク', choices=CommonConstant.GROWUPS, default=CommonConstant.GROWUP_G)
    up_str = models.IntegerField(u'力成長ランク', choices=CommonConstant.GROWUPS, default=CommonConstant.GROWUP_G)
    up_agi = models.IntegerField(u'敏捷成長ランク', choices=CommonConstant.GROWUPS, default=CommonConstant.GROWUP_G)
    up_mag = models.IntegerField(u'魔力成長ランク', choices=CommonConstant.GROWUPS, default=CommonConstant.GROWUP_G)
    up_unq = models.IntegerField(u'固有成長ランク', choices=CommonConstant.GROWUPS, default=CommonConstant.GROWUP_G)

    class Meta:
        verbose_name = u'種族'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(Race, self).save(*args, **kwargs)
        cache.delete(self._get_get_chices_list_cache_key())

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_chices_list_cache_key())
        super(Race, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_chices_list_cache_key(cls):
        return '%s/get_chices_list' % (cls._meta)

    @classmethod
    def get_chices_list(cls):
        cache_key =  cls._get_get_chices_list_cache_key()

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.all().values_list('id', 'name')
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l



# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import CachedBaseModel

from module.common.constant import CommonConstant

class BattleAction(CachedBaseModel):
    name = models.CharField(u'名称', max_length=100)
    comment = models.TextField(u'コメント', blank=True, default='')

    class Meta:
        verbose_name = u'バトルアクション'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(BattleAction, self).save(*args, **kwargs)
        cache.delete(self._get_get_chices_list_cache_key())

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_chices_list_cache_key())
        super(BattleAction, self).delete(*args, **kwargs)

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

class BattleTarget(CachedBaseModel):
    name = models.CharField(u'名称', max_length=100)
    comment = models.TextField(u'コメント', blank=True, default='')
    view_no = models.IntegerField(u'表示順', default=0)
    target_type = models.IntegerField(u'対象種別', default=CommonConstant.TARGET_TYPE_ENEMY, choices=CommonConstant.TARGET_TYPES)
    target_no = models.IntegerField(u'対象番号', default=0)

    class Meta:
        verbose_name = u'バトルターゲット'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(BattleTarget, self).save(*args, **kwargs)
        cache.delete(self._get_get_chices_list_cache_key())

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_chices_list_cache_key())
        super(BattleTarget, self).delete(*args, **kwargs)

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
            l = cls.objects.all().order_by('view_no')
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

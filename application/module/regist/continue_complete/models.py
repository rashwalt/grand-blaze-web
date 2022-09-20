# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import MultiRegistCachedModel

from module.regist.constant import RegistConstant

class ContinueComplete(MultiRegistCachedModel):
    """
    登録コンプリート
    """
    category = models.CharField(u'カテゴリ', max_length=100)

    class Meta:
        verbose_name = u'登録コンプリート'
        verbose_name_plural = verbose_name
        unique_together = (('user','category'),)

    def __unicode__(self):
        return  '%s-%s: ContinueComplete' % (self.user_id, self.category)

    def save(self, *args, **kwargs):
        super(ContinueComplete, self).save(*args, **kwargs)
        cache.delete(self._get_get_unique_cache_key(self.user_id, self.category))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_unique_cache_key(self.user_id, self.category))
        super(ContinueComplete, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_unique_cache_key(cls, user_id, category):
        return '%s/get_unique/%s/%s' % (cls._meta, user_id, category)

    @classmethod
    def get_unique(cls, user, category):
        cache_key = cls._get_get_unique_cache_key(user.id, category)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.get(user=user, category=category)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l
    
    @classmethod
    def completed(cls, user, category, ip_address, host, agent):
        continue_complete = cls.get_unique(user, category)
        if not continue_complete:
            ContinueComplete.objects.get_or_create(user=user, category=category, ip_address=ip_address, host_address=host, user_agent=agent)
        else:
            continue_complete.category = category
            continue_complete.save()
    
    @classmethod
    def get_last_entry(cls):
        return cls.objects.filter(updated_at__gte=(datetime.datetime.now() - datetime.timedelta(seconds=600))).values('user').distinct()
    
    @classmethod
    def get_last(cls, user):
        return cls.objects.filter(user=user, updated_at__gte=(datetime.datetime.now() - datetime.timedelta(seconds=600))).values_list('category', flat=True)
    
    @classmethod
    def get_categorys(cls, user):
        return cls.objects.filter(user=user).values_list('category', flat=True)



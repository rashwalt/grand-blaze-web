# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import CachedBaseModel

class Situation(CachedBaseModel):
    name = models.CharField(u'名称', max_length=100)
    it_comment = models.TextField(u'解説文', blank=True)

    class Meta:
        verbose_name = u'シチュエーション'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(Situation, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Situation, self).delete(*args, **kwargs)

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
            l = cls.objects.all()
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l


# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import User

from module.abstract.cachedmodels.models import CachedModel, CharacterCachedModel

class LinkCategory(CachedModel):
    name = models.CharField(u'カテゴリ名', max_length=250)
    
    class Meta:
        verbose_name = u'リンクカテゴリ'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(LinkCategory, self).save(*args, **kwargs)
        cache.delete(self._get_get_category_list_cache_key())

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_category_list_cache_key())
        super(LinkCategory, self).delete(*args, **kwargs)


    @classmethod
    def _get_get_category_list_cache_key(cls):
        return '%s/get_category_list' % cls._meta

    @classmethod
    def get_category_list(cls):
        cache_key = cls._get_get_category_list_cache_key()

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = list(cls.objects.all())
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class Link(CharacterCachedModel):
    
    name = models.CharField(u'サイト名', max_length=250)
    comment = models.CharField(u'サイト説明', max_length=400, blank=True)
    category = models.ForeignKey(LinkCategory, verbose_name=u'リンクカテゴリ')
    owner = models.CharField(u'オーナー名', max_length=200)
    url = models.CharField(u'URL', max_length=300)
    valid_fg = models.BooleanField(u'有効か', default=False)
    
    class Meta:
        verbose_name = u'リンク'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(Link, self).save(*args, **kwargs)
        cache.delete(self._get_get_category_top_cache_key(self.category_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_category_top_cache_key(self.category_id))
        super(Link, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_category_top_cache_key(cls, category):
        return '%s/get_category_top/category:%d' % (cls._meta, category)

    @classmethod
    def get_category_top(cls, category):
        cache_key =  cls._get_get_category_top_cache_key(category)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(category=category, valid_fg=True).order_by('created_at')
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l
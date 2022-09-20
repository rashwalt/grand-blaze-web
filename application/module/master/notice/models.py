# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import CachedModel

from module.master.notice.constant import NoticeConstant


class Notice(CachedModel):
    """
    お知らせ
    """
    
    title = models.CharField(u'タイトル', max_length=160)
    body = models.TextField(u'本文')
    category = models.IntegerField(u'カテゴリ', choices=NoticeConstant.CATEGORYS, default=NoticeConstant.CATEGORY_IMPORTANT)
    rank = models.IntegerField(u'表示優先度', default=50)
    view_date = models.DateTimeField(u'表示記事日', default=datetime.datetime.now())
    limit_date = models.DateTimeField(u'表示期限', null=True, blank=True)
    is_valid = models.BooleanField(u'有効')

    class Meta:
        verbose_name = u'お知らせ'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.title

    def save(self, *args, **kwargs):
        super(Notice, self).save(*args, **kwargs)
        cache.delete(self._get_get_top_cache_key(5))
        cache.delete(self._get_get_active_category_top_cache_key(self.category, None))
        cache.delete(self._get_get_category_top_cache_key(self.category, 10))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_top_cache_key(5))
        cache.delete(self._get_get_active_category_top_cache_key(self.category, None))
        cache.delete(self._get_get_category_top_cache_key(self.category, 10))
        super(Notice, self).delete(*args, **kwargs)
    
    @property
    def category_name(self):
        return NoticeConstant.get_category_name(self.category)

    @classmethod
    def _get_get_top_cache_key(cls, limit):
        return '%s/get_top/%s' % (cls._meta, limit)

    @classmethod
    def get_top(cls, limit):
        cache_key = cls._get_get_top_cache_key(limit)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(models.Q(is_valid=True), models.Q(category__lt=NoticeConstant.CATEGORY_TOPICS), models.Q(view_date__lte=datetime.datetime.now()), models.Q(limit_date__isnull=True)|models.Q(limit_date__gt=datetime.datetime.now())).order_by('-rank','-view_date')[:limit]
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

    @classmethod
    def _get_get_active_category_top_cache_key(cls, category, limit):
        return '%s/get_active_category_top/category:%d/%s' % (cls._meta, category, limit)

    @classmethod
    def get_active_category_top(cls, category, limit=5):
        cache_key = cls._get_get_active_category_top_cache_key(category, limit)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(models.Q(is_valid=True), models.Q(category=category), models.Q(view_date__lte=datetime.datetime.now()), models.Q(limit_date__isnull=True)|models.Q(limit_date__gt=datetime.datetime.now())).order_by('-rank','-view_date')[:limit]
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

    @classmethod
    def _get_get_category_top_cache_key(cls, category, limit):
        return '%s/get_category_top/category:%d/%s' % (cls._meta, category, limit)

    @classmethod
    def get_category_top(cls, category, limit=5):
        cache_key =  cls._get_get_category_top_cache_key(category, limit)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(is_valid=True, category=category).order_by('-rank','-view_date')
            if limit:
                l = l[:limit]
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

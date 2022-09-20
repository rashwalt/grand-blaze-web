# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import User

class CachedBaseModel(models.Model):
    """
    キャッシュサポートモデル抽象クラス
    """

    class Meta:
        abstract=True

    def save(self, *args, **kwargs):
        super(CachedBaseModel, self).save(*args, **kwargs)
        cache.delete(self._get_get_cache_key(self.pk))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_cache_key(self.pk))
        super(CachedBaseModel, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_cache_key(cls, key_id):
        return '%s/GET/%s' % (cls._meta, key_id)

    @classmethod
    def get(cls, key_id):
        cache_key = cls._get_get_cache_key(key_id)

        v = cache.get(cache_key, None)

        if v:
            return v

        try:
            v = cls.objects.get(pk=key_id)
            cache.set(cache_key, v, 3600)
        except:
            pass

        return v

class CachedModel(CachedBaseModel):
    """
    キャッシュサポートモデル抽象クラス
    """
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now_add=True, auto_now=True)

    class Meta:
        abstract=True

class RegistCachedModel(CachedModel):
    """
    キャッシュサポートモデル抽象クラス
    """
    user = models.ForeignKey(User, verbose_name=u'登録者', primary_key=True)
    
    ip_address = models.IPAddressField(u'IPアドレス', blank=True)
    host_address = models.CharField(u'ホスト名', max_length=400, blank=True)
    user_agent = models.CharField(u'ユーザーエージェント', max_length=400, blank=True)

    class Meta:
        abstract=True

class MultiRegistCachedModel(CachedModel):
    """
    キャッシュサポートモデル抽象クラス
    """
    user = models.ForeignKey(User, verbose_name=u'登録者')

    ip_address = models.IPAddressField(u'IPアドレス', blank=True)
    host_address = models.CharField(u'ホスト名', max_length=400, blank=True)
    user_agent = models.CharField(u'ユーザーエージェント', max_length=400, blank=True)

    class Meta:
        abstract=True

    def save(self, *args, **kwargs):
        super(MultiRegistCachedModel, self).save(*args, **kwargs)
        cache.delete(self._get_filter_cache_key(self.user_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_filter_cache_key(self.user_id))
        super(MultiRegistCachedModel, self).delete(*args, **kwargs)

    @classmethod
    def _get_filter_cache_key(cls, user_id):
        return '%s/FILTER/%s' % (cls._meta, user_id)

    @classmethod
    def get_filter_by_user(cls, user_id):
        cache_key = cls._get_filter_cache_key(user_id)

        l = cache.get(cache_key, None)

        if l:
            return l

        try:
            l = list(cls.objects.filter(user=user_id))
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class CharacterCachedModel(CachedModel):
    """
    キャッシュサポートモデル抽象クラス
    """
    user = models.ForeignKey(User, verbose_name=u'登録者', primary_key=True)

    class Meta:
        abstract=True

class MultiCharacterCachedModel(CachedModel):
    """
    キャッシュサポートモデル抽象クラス
    """
    user = models.ForeignKey(User, verbose_name=u'登録者')

    class Meta:
        abstract=True

    def save(self, *args, **kwargs):
        super(MultiCharacterCachedModel, self).save(*args, **kwargs)
        cache.delete(self._get_filter_cache_key(self.user_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_filter_cache_key(self.user_id))
        super(MultiCharacterCachedModel, self).delete(*args, **kwargs)

    @classmethod
    def _get_filter_cache_key(cls, user_id):
        return '%s/FILTER/%s' % (cls._meta, user_id)

    @classmethod
    def get_filter_by_user(cls, user):
        cache_key = cls._get_filter_cache_key(user.id)

        l = cache.get(cache_key, None)

        if l:
            return l

        try:
            l = list(cls.objects.filter(user=user))
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l
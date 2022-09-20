# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import User

from module.abstract.cachedmodels.models import CachedModel

from module.character.models import Character

class UserProfile(models.Model):
    """
    ユーザープロファイル
    """
    
    user = models.ForeignKey(User, verbose_name=u'ユーザー', unique=True, primary_key=True)
    user_name = models.CharField(u'アカウント名', max_length=80, blank=True)
    entry_id = models.IntegerField(u'エントリー番号', null=True, blank=True)
    official_news = models.BooleanField(u'公式からのメールでのお知らせ受取', blank=True, default=True)
    continue_mail = models.BooleanField(u'各種登録内容受取', blank=True, default=True)
    message_mail = models.BooleanField(u'未読メッセージ受取', blank=True, default=True)
    pass_activate = models.CharField(u'アクティベートハッシュ', max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now_add=True, auto_now=True)

    class Meta:
        verbose_name = u'ユーザープロファイル'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.user_name

    @classmethod
    def check_and_get_active_records(cls, activate_hash):
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        profile = None
        
        try:
            profile = UserProfile.objects.get(pass_activate=activate_hash, created_at__gt=yesterday)
        except:
            pass
        
        if profile:
            return profile.user
        return None
        

class InstantMessage(CachedModel):
    
    user = models.ForeignKey(User, verbose_name=u'ユーザー', related_name='user_instant_message')
    from_user = models.ForeignKey(User, verbose_name=u'送信元ユーザー', related_name='from_user_instant_message')
    title = models.CharField(u'タイトル', max_length=140)
    body = models.TextField(u'本文')
    read_complete = models.BooleanField(u'既読か', default=False)
    
    class Meta:
        verbose_name = u'インスタントメッセージ'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.title

    def save(self, *args, **kwargs):
        super(InstantMessage, self).save(*args, **kwargs)
        cache.delete(self._get_get_to_user_list_cache_key(self.user_id))
        cache.delete(self._get_get_from_user_list_cache_key(self.from_user_id))
        cache.delete(self._get_get_read_complete_count_cache_key(self.user_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_to_user_list_cache_key(self.user_id))
        cache.delete(self._get_get_from_user_list_cache_key(self.from_user_id))
        cache.delete(self._get_get_read_complete_count_cache_key(self.user_id))
        super(InstantMessage, self).delete(*args, **kwargs)
    
    def get_from_user_name(self):
        profile = None
        user = self.from_user
        try:
            profile = user.get_profile()
        except UserProfile.DoesNotExist:
            pass
        
        if profile:
            return profile.user_name
        return ''
    
    def get_to_user_name(self):
        profile = None
        user = self.user
        try:
            profile = user.get_profile()
        except UserProfile.DoesNotExist:
            pass
        
        if profile:
            return profile.user_name
        return ''
    
    @property
    def from_character_name(self):
        chara = Character.get(self.from_user_id)
        if chara:
            return chara.nick_name
        else:
            return ''
    
    @property
    def to_character_name(self):
        chara = Character.get(self.user_id)
        if chara:
            return chara.nick_name
        else:
            return ''

    @classmethod
    def _get_get_to_user_list_cache_key(cls, user_id):
        return '%s/get_to_user_list/%s' % (cls._meta, user_id)

    @classmethod
    def get_to_user_list(cls, user):
        cache_key = cls._get_get_to_user_list_cache_key(user.id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(user=user).order_by('read_complete','-created_at')
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

    @classmethod
    def _get_get_from_user_list_cache_key(cls, user_id):
        return '%s/get_from_user_list/%s' % (cls._meta, user_id)

    @classmethod
    def get_from_user_list(cls, user):
        cache_key = cls._get_get_from_user_list_cache_key(user.id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(from_user=user).order_by('-created_at')
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

    @classmethod
    def _get_get_read_complete_count_cache_key(cls, user_id):
        return '%s/get_read_complete_count/%s' % (cls._meta, user_id)

    @classmethod
    def get_read_complete_count(cls, user):
        if not user.is_authenticated():
            return None

        cache_key = cls._get_get_read_complete_count_cache_key(user.id)

        v = cache.get(cache_key)
        if v:
            return v

        v = cls.objects.filter(user=user, read_complete=False).count()
        cache.set(cache_key, v, 3600)

        return v
    
    @classmethod
    def get_last(cls):
        return cls.objects.filter(read_complete=False, updated_at__gte=(datetime.datetime.now() - datetime.timedelta(seconds=3600))).values('user').distinct()


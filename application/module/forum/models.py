# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.core.cache import cache
from django.contrib.auth.models import User

from module.abstract.cachedmodels.models import CachedBaseModel, CachedModel

from module.account.api import UserProfileAPI

from module.forum.constant import ForumConstant
from module.character.models import Character

class Forum(CachedBaseModel):
    """
    フォーラムリスト
    """
    name = models.CharField(u'名称', max_length=140)
    parent_forum = models.ForeignKey('self', verbose_name=u'親フォーラム', related_name='parent_forum_forum', null=True, blank=True)
    is_not_auth = models.BooleanField(u'未登録投稿の許可', default=False)

    class Meta:
        verbose_name = u'フォーラムリスト'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(Forum, self).save(*args, **kwargs)
        cache.delete(self._get_get_forum_list_cache_key())
        cache.delete(self._get_get_forum_choice_list_cache_key())

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_forum_list_cache_key())
        cache.delete(self._get_get_forum_choice_list_cache_key())
        super(Forum, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_forum_list_cache_key(cls):
        return '%s/get_forum_list' % cls._meta

    @classmethod
    def get_forum_list(cls):
        cache_key = cls._get_get_forum_list_cache_key()

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = list(Forum.objects.all())
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

    @classmethod
    def _get_get_forum_choice_list_cache_key(cls):
        return '%s/get_forum_choice_list' % cls._meta

    @classmethod
    def get_forum_choice_list(cls):
        cache_key = cls._get_get_forum_choice_list_cache_key()

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = list(Forum.objects.all().values_list('id', 'name'))
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class ForumStatus(CachedBaseModel):
    """
    フォーラムステータス
    """
    forum = models.ForeignKey(Forum, verbose_name=u'フォーラム', related_name='forum_forum_status')
    name = models.CharField(u'ステータス名', max_length=10)
    is_staff_only = models.BooleanField(u'スタッフ権限のみ表示か', default=False)
    is_new_thread = models.BooleanField(u'新規作成時のみ表示か', default=False)
    is_thread_rock = models.BooleanField(u'スレッドロック', default=False)

    class Meta:
        verbose_name = u'フォーラムステータス'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(ForumStatus, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(ForumStatus, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_status_list_cache_key(cls, forum_id, is_staff, is_create, is_lock):
        return '%s/get_status_list/%s/%s/%s/%s' % (cls._meta, forum_id, is_staff, is_create, is_lock)

    @classmethod
    def get_status_list(cls, forum_id, request, is_create=False, is_lock=False):
        is_staff = request.user.is_staff

        cache_key = cls._get_get_status_list_cache_key(forum_id, is_staff, is_create, is_lock)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.values_list('id', 'name').filter(forum=forum_id)
            if not is_staff:
                l = l.filter(is_staff_only=False)
            if is_create:
                l = l.filter(is_new_thread=True, is_thread_rock=False)
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class Thread(CachedModel):
    """
    スレッド
    """
    forum = models.ForeignKey(Forum, verbose_name=u'フォーラム', related_name='forum_forum')
    title = models.CharField(u'スレッド名', max_length=140)
    create_user_id = models.PositiveIntegerField(u'作成者', default=0)
    create_user_name = models.CharField(u'作成者名', max_length=140, blank=True, null=True)
    view_count = models.IntegerField(u'表示数', default=0)
    is_rock = models.BooleanField(u'スレッドのロック', default=False)
    thread_solid = models.BooleanField(u'固定スレッド', default=False)
    forum_status = models.ForeignKey(ForumStatus, verbose_name=u'ステータス', related_name='forum_status_forum_status')
    status_change_pass = models.CharField(u'ステータス変更パスワード', max_length=16, blank=True, null=True)
    last_article_update_at = models.DateTimeField(u'最終投稿日時', default=datetime.datetime.now())

    class Meta:
        verbose_name = u'スレッド'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: %s' % (self.id, self.title)

    def save(self, *args, **kwargs):
        super(Thread, self).save(*args, **kwargs)
        cache.delete(self._get_get_thread_list_cache_key(self.forum_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_thread_list_cache_key(self.forum_id))
        super(Thread, self).delete(*args, **kwargs)
        
    @property
    def create_user(self):
        try:
            return User.objects.get(id=self.create_user_id)
        except:
            return None
    
    def get_create_user_name(self):
        if self.create_user_id and self.create_user:
            return UserProfileAPI.get_user_name(self.create_user)
        return ''
    
    def get_article_count(self):
        from module.forum.api import ArticleAPI
        return ArticleAPI.get_count(self.id)

    def get_forum_status_name(self):
        from module.forum.api import ForumStatusAPI
        return ForumStatusAPI.get_name(self.forum_status_id)

    @classmethod
    def _get_get_thread_list_cache_key(cls, forum_id):
        return '%s/get_thread_list/%s' % (cls._meta, forum_id)

    @classmethod
    def get_thread_list(cls, forum_id):
        cache_key = cls._get_get_thread_list_cache_key(forum_id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = Thread.objects.filter(forum=forum_id).order_by('-thread_solid', 'is_rock','-updated_at','forum_status')
            l = list(l)
            cache.set(cache_key, l, 60 * 60)
        except:
            pass

        return l
    
    @classmethod
    def update_view_count(cls, thread_id):
        cls.objects.filter(pk=thread_id).update(view_count=models.F('view_count') + 1)
        thread_data = cls.get(thread_id)
        cache.delete(cls._get_get_thread_list_cache_key(thread_data.forum_id))

class Article(CachedModel):
    """
    記事
    """
    forum_id = models.PositiveIntegerField(u'フォーラム', default=0)
    thread = models.ForeignKey(Thread, verbose_name=u'親スレッド', related_name='thread_thread')
    body = models.TextField(u'本文')
    user_id = models.PositiveIntegerField(u'投稿者', default=0)
    user_name = models.CharField(u'投稿者名', max_length=140, blank=True, null=True)
    is_delete = models.BooleanField(u'削除フラグ', default=False)
    delete_user_id = models.PositiveIntegerField(u'削除した人', null=True, blank=True, default=None)
    delete_mean = models.TextField(u'削除理由', null=True, blank=True)
    is_edit = models.BooleanField(u'編集フラグ', default=False)
    edit_mean = models.TextField(u'編集理由', null=True, blank=True)
    edit_at = models.DateTimeField(u'最終編集日時', default=datetime.datetime.now())
    good_list = models.TextField(u'いいねリスト', null=True, blank=True)

    class Meta:
        verbose_name = u'記事'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.body
    
    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        cache.delete(self._get_get_count_cache_key(self.thread_id))
        cache.delete(self._get_get_article_list_cache_key(self.thread_id, True))
        cache.delete(self._get_get_article_list_cache_key(self.thread_id, False))
        cache.delete(self._get_get_lastest_article_list_cache_key())

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_count_cache_key(self.thread_id))
        cache.delete(self._get_get_article_list_cache_key(self.thread_id, True))
        cache.delete(self._get_get_article_list_cache_key(self.thread_id, False))
        cache.delete(self._get_get_lastest_article_list_cache_key())
        super(Article, self).delete(*args, **kwargs)
        
    @property
    def user(self):
        try:
            return User.objects.get(id=self.user_id)
        except:
            return None
        
    @property
    def delete_user(self):
        try:
            return User.objects.get(id=self.delete_user_id)
        except:
            return None
    
    @property
    def good_count(self):
        if not self.good_list:
            return 0
        go_list = self.good_list.split(',')
        return len(go_list)
    
    @property
    def b_thread(self):
        return Thread.get(self.thread_id)
    
    @property
    def character_name(self):
        chara = Character.get(self.user_id)
        if chara:
            return chara.nick_name
        else:
            return ''

    def get_user_name(self):
        if self.user_id and self.user:
            return UserProfileAPI.get_user_name_only(self.user)
        return ''

    def get_delete_user_name(self):
        if self.delete_user_id and self.delete_user:
            return UserProfileAPI.get_user_name(self.delete_user)
        return ''

    @classmethod
    def _get_get_count_cache_key(cls, thread_id):
        return '%s/get_count/%s' % (cls._meta, thread_id)
    
    @classmethod
    def get_count(cls, thread_id):
        cache_key = cls._get_get_count_cache_key(thread_id)
        
        v = cache.get(cache_key, 0)
        if v:
            return v
        
        try:
            v = cls.objects.filter(thread=thread_id, is_delete=False).count()
            if v:
                v -= 1
            cache.set(cache_key, v)
        except:
            pass
        
        return v

    @classmethod
    def _get_get_article_list_cache_key(cls, thread_id, is_last):
        return '%s/get_article_list/%s/%s' % (cls._meta, thread_id, is_last)

    @classmethod
    def get_article_list(cls, thread_id, is_last=False):
        cache_key = cls._get_get_article_list_cache_key(thread_id, is_last)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            if is_last:
                l = cls.objects.filter(thread=thread_id).order_by('-id')[:10]
            else:
                l = cls.objects.filter(thread=thread_id).order_by('id')
            l = list(l)
            if is_last:
                l.reverse()
            cache.set(cache_key, l, 60 * 60)
        except:
            pass

        return l

    @classmethod
    def get_search_article_list(cls, forum_id, choice_type, words_list):
        queries = [models.Q(body__icontains=word) for word in words_list]
        if not queries:
            return []
        query = queries.pop()
        if choice_type == ForumConstant.CHOICE_TYPE_OR:
            for item in queries:
                query |= item
        else:
            for item in queries:
                query &= item

        l = []

        try:
            l = cls.objects.filter(query).filter(is_delete=False).order_by('-created_at')
            if forum_id:
                l = l.filter(forum_id=forum_id)
            l = l.filter(is_delete=False)
            l = list(l)
        except:
            pass

        return l
    
    @classmethod
    def update_good_count(cls, article_id, user):
        article_data = cls.get(article_id)
        if article_data:
            if article_data.good_list:
                go_list = article_data.good_list.split(',')
            else:
                go_list = []
            user_id = str(user.id)
            if not user_id in go_list:
                go_list.append(user_id)
            article_data.good_list = ','.join(go_list)
            article_data.save()
        return len(go_list)

    @classmethod
    def _get_get_lastest_article_list_cache_key(cls):
        return '%s/get_lastest_article_list' % (cls._meta)

    @classmethod
    def get_lastest_article_list(cls, limit=5):
        
        cache_key = cls._get_get_lastest_article_list_cache_key()

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(is_delete=False).order_by('-updated_at')[:limit]
            l = list(l)
            cache.set(cache_key, l, 60 * 60)
        except:
            pass

        return l


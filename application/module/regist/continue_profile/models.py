# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import RegistCachedModel

from module.regist.constant import RegistConstant
from module.master.install.models import Install

class ContinueProfile(RegistCachedModel):
    """
    個人設定
    """
    nick_name = models.CharField(u'愛称', max_length=80, null=True, blank=True)
    age = models.IntegerField(u'年齢', null=True, blank=True)
    height = models.IntegerField(u'身長', null=True, blank=True)
    weight = models.IntegerField(u'体重', null=True, blank=True)
    profile = models.TextField(u'プロフィール', null=True, blank=True)
    image_url = models.CharField(u'イメージURL', max_length=255, blank=True)
    image_width = models.PositiveIntegerField(u'イメージ横サイズ', null=True, blank=True)
    image_height = models.PositiveIntegerField(u'イメージ縦サイズ', null=True, blank=True)
    image_link_url = models.CharField(u'イメージリンクURL', max_length=255, blank=True)
    image_copyright = models.CharField(u'イメージ権利表記', max_length=180, blank=True)
    unique_name = models.CharField(u'ユニーク名', max_length=36, null=True, blank=True)
    account_status = models.IntegerField(u'アカウントステータス', null=True, blank=True, default=RegistConstant.ACCOUNT_STAT_ACTIVE, choices=RegistConstant.ACCOUNT_STATUS)

    class Meta:
        verbose_name = u'個人設定'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: ContinueProfile' % self.user_id

    def save(self, *args, **kwargs):
        super(ContinueProfile, self).save(*args, **kwargs)
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))

    def delete(self, *args, **kwargs):
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))
        super(ContinueProfile, self).delete(*args, **kwargs)
    


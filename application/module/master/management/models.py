# -*- coding: utf-8 -*-

from django.db import models

from module.abstract.cachedmodels.models import CachedBaseModel

class Management(CachedBaseModel):
    """
    サイトマネージャー
    """
    is_regist_stop = models.BooleanField(u'登録処理可能か', default=False)

    class Meta:
        verbose_name = u'サイトマネージャー'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  str(self.id)
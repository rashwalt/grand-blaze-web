# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import MultiRegistCachedModel

from module.regist.constant import RegistConstant
from module.character.models import Character

class ContinueMessage(MultiRegistCachedModel):
    """
    メッセージ登録
    """
    mes_no = models.IntegerField(u'メッセージNo', default=1, blank=True)
    message_target = models.IntegerField(u'メッセージ対象', default=RegistConstant.MESSAGE_TARGET_PRIVATE, choices=RegistConstant.MESSAGE_TARGETS)
    message_entry = models.IntegerField(u'送信相手No', null=True, blank=True)
    message_body = models.TextField(u'メッセージ内容', blank=True)

    class Meta:
        verbose_name = u'メッセージ登録'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s-%s: ContinueMessage' % (self.user_id, self.mes_no)

    def save(self, *args, **kwargs):
        super(ContinueMessage, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(ContinueMessage, self).delete(*args, **kwargs)
    
    @property
    def message_entry_ch(self):
        return Character.get(self.message_entry)

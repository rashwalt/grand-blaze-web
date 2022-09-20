# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import MultiRegistCachedModel

from module.regist.constant import RegistConstant

class ContinueIcon(MultiRegistCachedModel):
    """
    アイコン設定
    """
    icon_id = models.IntegerField(u'アイコンNo', default=1, blank=True)
    icon_url = models.CharField(u'アイコンURL', max_length=255)
    icon_copyright = models.CharField(u'アイコン著作者', max_length=180)

    class Meta:
        verbose_name = u'アイコン設定'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s-%s: ContinueIcon' % (self.user_id, self.icon_id)

    def save(self, *args, **kwargs):
        super(ContinueIcon, self).save(*args, **kwargs)
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))

    def delete(self, *args, **kwargs):
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))
        super(ContinueIcon, self).delete(*args, **kwargs)

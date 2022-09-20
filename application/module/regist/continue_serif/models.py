# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import MultiRegistCachedModel, MultiCharacterCachedModel, CachedModel

from module.regist.constant import RegistConstant

from module.master.situation.models import Situation
from module.master.skill.models import Skill

class ContinueSerif(MultiRegistCachedModel):
    """
    セリフ設定
    """
    word_no = models.IntegerField(u'セリフNo', default=1, blank=True)
    situation_id = models.IntegerField(u'シチュエーション')
    serif_text = models.TextField(u'セリフ内容')
    perks_id = models.IntegerField(u'スキルID', null=True, blank=True)

    class Meta:
        verbose_name = u'セリフ設定'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s-%s: ContinueSerif' % (self.user_id, self.word_no)

    def save(self, *args, **kwargs):
        super(ContinueSerif, self).save(*args, **kwargs)
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))

    def delete(self, *args, **kwargs):
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))
        super(ContinueSerif, self).delete(*args, **kwargs)
        
    @property
    def situation(self):
        return Situation.get(self.situation_id)
    
    @property
    def skill(self):
        return Skill.get(self.perks_id)


class SavingSerifHead(MultiCharacterCachedModel):
    """
    保存中のセリフ・ヘッド
    """
    name = models.CharField(u'名前', max_length=100)

    class Meta:
        verbose_name = u'保存セリフ・ヘッド'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s-%s: SavingSerifHead' % (self.user_id, self.name)
    
    def save(self, *args, **kwargs):
        super(SavingSerifHead, self).save(*args, **kwargs)
        cache.delete(self._get_filter_values_cache_key(self.user_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_filter_values_cache_key(self.user_id))
        super(SavingSerifHead, self).delete(*args, **kwargs)

    @classmethod
    def _get_filter_values_cache_key(cls, user_id):
        return '%s/FILTER_VALUES/%s' % (cls._meta, user_id)

    @classmethod
    def get_filter_by_user_values(cls, user):
        cache_key = cls._get_filter_values_cache_key(user.id)

        l = cache.get(cache_key, None)

        if l:
            return l

        try:
            l = list(cls.objects.filter(user=user).values_list('id', 'name'))
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

    @classmethod
    def _get_get_values_cache_key(cls, saving_id):
        return '%s/get_values/%s' % (cls._meta, saving_id)

    @classmethod
    def get_values(cls, saving_id):
        cache_key = cls._get_get_values_cache_key(saving_id)

        l = cache.get(cache_key, None)

        if l:
            return l

        try:
            l = list(cls.objects.filter(id=saving_id).values_list('id', 'name'))
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class SavingSerifBody(CachedModel):
    """
    保存中のセリフ・ボディ
    """
    saving_action = models.ForeignKey(SavingSerifHead, verbose_name=u'戦術ヘッド', db_index=True)
    word_no = models.IntegerField(u'セリフNo', default=1, blank=True)
    situation_id = models.IntegerField(u'シチュエーション')
    serif_text = models.TextField(u'セリフ内容')
    perks_id = models.IntegerField(u'スキルID', null=True, blank=True)

    class Meta:
        verbose_name = u'保存セリフ・ボディ'
        verbose_name_plural = verbose_name
        unique_together = (('saving_action','word_no'),)

    def __unicode__(self):
        return  '%s-%s: SavingSerifBody' % (self.user_id, self.saving_action_id)
    
    def save(self, *args, **kwargs):
        super(SavingSerifBody, self).save(*args, **kwargs)
        cache.delete(self._get_get_unique_list_cache_key(self.saving_action_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_unique_list_cache_key(self.saving_action_id))
        super(SavingSerifBody, self).delete(*args, **kwargs)
        
    @property
    def situation(self):
        return Situation.get(self.situation_id)
    
    @property
    def skill(self):
        return Skill.get(self.perks_id)

    @classmethod
    def _get_get_unique_list_cache_key(cls, saving_id):
        return '%s/get_unique_list/%s' % (cls._meta, saving_id)

    @classmethod
    def get_unique_list(cls, saving_id):
        cache_key = cls._get_get_unique_list_cache_key(saving_id)

        l = cache.get(cache_key, None)

        if l:
            return l

        try:
            l = list(cls.objects.filter(saving_action=saving_id).values('saving_action', 'word_no', 'situation_id', 'serif_text', 'perks_id').order_by('situation_id', 'id'))
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l
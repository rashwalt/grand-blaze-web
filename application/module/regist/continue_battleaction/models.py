# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import MultiRegistCachedModel, MultiCharacterCachedModel, CachedModel

from module.master.battleaction.models import BattleAction, BattleTarget
from module.master.skill.models import Skill

from module.regist.constant import RegistConstant

class ContinueBattleAction(MultiRegistCachedModel):
    """
    戦術登録
    """
    action_no = models.IntegerField(u'行動No', default=1, blank=True)
    action_target = models.IntegerField(u'バトルターゲット')
    action = models.IntegerField(u'バトルアクション', default=0)
    perks_id = models.IntegerField(u'スキルID', null=True, blank=True)

    class Meta:
        verbose_name = u'戦術登録'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s-%s: ContinueBattleAction' % (self.user_id, self.action_no)

    def save(self, *args, **kwargs):
        super(ContinueBattleAction, self).save(*args, **kwargs)
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))

    def delete(self, *args, **kwargs):
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))
        super(ContinueBattleAction, self).delete(*args, **kwargs)
    
    @property
    def target(self):
        return BattleTarget.get(self.action_target)
    
    @property
    def action_data(self):
        return BattleAction.get(self.action)
    
    @property
    def skill(self):
        return Skill.get(self.perks_id)

class SavingActionHead(MultiCharacterCachedModel):
    """
    保存中の戦術・ヘッド
    """
    name = models.CharField(u'名前', max_length=100)

    class Meta:
        verbose_name = u'保存戦術・ヘッド'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s-%s: SavingActionHead' % (self.user_id, self.name)
    
    def save(self, *args, **kwargs):
        super(SavingActionHead, self).save(*args, **kwargs)
        cache.delete(self._get_filter_values_cache_key(self.user_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_filter_values_cache_key(self.user_id))
        super(SavingActionHead, self).delete(*args, **kwargs)

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

class SavingActionBody(CachedModel):
    """
    保存中の戦術・ボディ
    """
    saving_action = models.ForeignKey(SavingActionHead, verbose_name=u'戦術ヘッド', db_index=True)
    action_no = models.IntegerField(u'行動No', default=1, blank=True)
    action_target = models.IntegerField(u'バトルターゲット', null=True)
    action = models.IntegerField(u'バトルアクション', default=0, null=True)
    perks_id = models.IntegerField(u'スキルID', null=True, blank=True)

    class Meta:
        verbose_name = u'保存戦術・ボディ'
        verbose_name_plural = verbose_name
        unique_together = (('saving_action','action_no'),)

    def __unicode__(self):
        return  '%s-%s: SavingActionBody' % (self.user_id, self.saving_action_id)
    
    def save(self, *args, **kwargs):
        super(SavingActionBody, self).save(*args, **kwargs)
        cache.delete(self._get_get_unique_list_cache_key(self.saving_action_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_unique_list_cache_key(self.saving_action_id))
        super(SavingActionBody, self).delete(*args, **kwargs)

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
            l = list(cls.objects.filter(saving_action=saving_id).values('saving_action', 'action_no', 'action_target', 'action', 'perks_id'))
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

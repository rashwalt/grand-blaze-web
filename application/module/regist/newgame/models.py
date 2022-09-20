# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import RegistCachedModel

from module.regist.constant import RegistConstant

from module.master.install.models import Install
from module.master.race.models import Race

class NewGame(RegistCachedModel):
    """
    ニューゲーム
    """
    character_name = models.CharField(u'キャラクター名', max_length=250)
    nick_name = models.CharField(u'愛称', max_length=80)
    sex = models.PositiveSmallIntegerField(u'性別', choices=RegistConstant.SEXS, default=RegistConstant.SEX_UNKNOWN)
    age = models.IntegerField(u'年齢')
    height = models.IntegerField(u'身長')
    weight = models.IntegerField(u'体重')
    nation_id = models.PositiveIntegerField(u'所属国', choices=RegistConstant.NATIONS, default=RegistConstant.NATION_FARNELD)
    image_url = models.CharField(u'イメージURL', max_length=255, blank=True)
    image_width = models.PositiveIntegerField(u'イメージ横サイズ', null=True, blank=True)
    image_height = models.PositiveIntegerField(u'イメージ縦サイズ', null=True, blank=True)
    image_link_url = models.CharField(u'イメージリンクURL', max_length=255, blank=True)
    image_copyright = models.CharField(u'イメージ権利表記', max_length=180, blank=True)
    install_class_id = models.PositiveIntegerField(u'インストールクラス', default=1)
    race_id = models.PositiveIntegerField(u'種族', default=1)
    guardian_id = models.PositiveIntegerField(u'守護者', choices=RegistConstant.GUARDIANS, default=RegistConstant.GUARDIAN_IGNIS)
    weapon_id = models.PositiveIntegerField(u'武器', choices=RegistConstant.WEAPONS, default=RegistConstant.WEAPON_HANDS)
    unique_name = models.CharField(u'ユニーク名', max_length=36)
    activate = models.IntegerField(u'アクティベート', default=0)

    class Meta:
        verbose_name = u'ニューゲーム'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: NewGame' % self.user_id

    def save(self, *args, **kwargs):
        super(NewGame, self).save(*args, **kwargs)
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))

    def delete(self, *args, **kwargs):
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))
        super(NewGame, self).delete(*args, **kwargs)
    
    @property
    def install_class(self):
        return Install.get(self.install_class_id)
    
    @property
    def race(self):
        return Race.get(self.race_id)
# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import RegistCachedModel

from module.regist.constant import RegistConstant
from module.character.models import Character, CharacterHavingItem
from module.master.install.models import Install

class ContinueEquip(RegistCachedModel):
    """
    戦闘準備登録
    """
    install = models.IntegerField(u'メインインストール', default=0, blank=True)
    secondary_install = models.IntegerField(u'サブインストール', default=0, blank=True)
    equip_main = models.IntegerField(u'メイン装備', default=None, blank=True, null=True)
    equip_sub = models.IntegerField(u'サブ装備', default=None, blank=True, null=True)
    equip_head = models.IntegerField(u'頭装備', default=None, blank=True, null=True)
    equip_body = models.IntegerField(u'身体装備', default=None, blank=True, null=True)
    equip_acce1 = models.IntegerField(u'アクセサリ装備', default=None, blank=True, null=True)
    formation = models.IntegerField(u'隊列', default=RegistConstant.FORMATION_STAY, choices=RegistConstant.FORMATIONS)
    

    class Meta:
        verbose_name = u'戦闘準備登録'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: ContinueMain' % self.user_id

    def save(self, *args, **kwargs):
        super(ContinueEquip, self).save(*args, **kwargs)
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))

    def delete(self, *args, **kwargs):
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))
        super(ContinueEquip, self).delete(*args, **kwargs)
    
    @property
    def main_install(self):
        return Install.get(self.install)
    
    @property
    def sub_install(self):
        return Install.get(self.secondary_install)
    
    @property
    def equip_main_it(self):
        return CharacterHavingItem.get_filter_by_haved(self.user, self.equip_main)
    
    @property
    def equip_sub_it(self):
        return CharacterHavingItem.get_filter_by_haved(self.user, self.equip_sub)
    
    @property
    def equip_head_it(self):
        return CharacterHavingItem.get_filter_by_haved(self.user, self.equip_head)
    
    @property
    def equip_body_it(self):
        return CharacterHavingItem.get_filter_by_haved(self.user, self.equip_body)
    
    @property
    def equip_acce1_it(self):
        return CharacterHavingItem.get_filter_by_haved(self.user, self.equip_acce1)
    
    @property
    def is_equip_main(self):
        return int(self.equip_main)
    
    @property
    def is_equip_sub(self):
        return int(self.equip_sub)
    
    @property
    def is_equip_head(self):
        return int(self.equip_head)
    
    @property
    def is_equip_body(self):
        return int(self.equip_body)
    
    @property
    def is_equip_acce1(self):
        return int(self.equip_acce1)


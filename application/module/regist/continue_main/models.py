# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import RegistCachedModel

from module.regist.constant import RegistConstant
from module.master.quest.models import Quest, Mark
from module.character.models import Character, CharacterHavingItem, CharacterQuest
from module.master.skill.models import Skill
from module.master.quest.constant import QuerstConstant
from module.master.quest.models import FieldType

class ContinueMain(RegistCachedModel):
    """
    継続登録
    """
    party_secession = models.IntegerField(u'パーティ編成', default=RegistConstant.PARTY_SECESSION_STAY, choices=RegistConstant.PARTY_SECESSIONS)
    pcm_add_1 = models.IntegerField(u'誘う相手1', default=None, blank=True, null=True)
    pcm_add_2 = models.IntegerField(u'誘う相手2', default=None, blank=True, null=True)
    pcm_add_3 = models.IntegerField(u'誘う相手3', default=None, blank=True, null=True)
    pcm_add_4 = models.IntegerField(u'誘う相手4', default=None, blank=True, null=True)
    pcm_add_5 = models.IntegerField(u'誘う相手5', default=None, blank=True, null=True)
    party_hope = models.IntegerField(u'パーティ参加希望', default=RegistConstant.PARTY_HOPE_STAY, choices=RegistConstant.PARTY_HOPES)
    option_comes_no = models.IntegerField(u'特定相手からのみ誘いを受ける', default=None, blank=True, null=True)
    party_name = models.CharField(u'パーティ名', max_length=80, blank=True)
    quest_id = models.IntegerField(u'クエスト', default=0)
    mark_id = models.IntegerField(u'マーク', default=0)
    use_item_1 = models.IntegerField(u'使用アイテム1', default=None, blank=True, null=True)
    use_item_1_message = models.CharField(u'アイテム使用メッセージ1', max_length=200, blank=True)
    use_item_2 = models.IntegerField(u'使用アイテム2', default=None, blank=True, null=True)
    use_item_2_message = models.CharField(u'アイテム使用メッセージ2', max_length=200, blank=True)
    use_item_3 = models.IntegerField(u'使用アイテム3', default=None, blank=True, null=True)
    use_item_3_message = models.CharField(u'アイテム使用メッセージ3', max_length=200, blank=True)
    getting_private_skill = models.IntegerField(u'プライベートスキル取得', default=None, null=True, blank=True)

    class Meta:
        verbose_name = u'継続登録'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: ContinueMain' % self.user_id

    def save(self, *args, **kwargs):
        super(ContinueMain, self).save(*args, **kwargs)
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))

    def delete(self, *args, **kwargs):
        #cache.delete(self._get_get_thread_list_cache_key(self.forum_id))
        super(ContinueMain, self).delete(*args, **kwargs)
    
    @property
    def quest(self):
        return Quest.get(self.quest_id)
    
    @property
    def quest_name(self):
        quest = self.quest
        
        complete_quest_ids = CharacterQuest.get_chices_list(self.user, 1)
        complete_quest_ids.append(0)
        
        quest_type_name = u'クエスト'
        if quest.quest_type == QuerstConstant.QUEST_TYPE_MISSION:
            quest_type_name = u'ミッション'
        elif quest.quest_type == QuerstConstant.QUEST_TYPE_EVENT:
            quest_type_name = u'イベント'
        if quest.id == 0:
            return u'%s' % quest.name
        else:
            cleard = u''
            if quest.id in complete_quest_ids:
                cleard = u'《済》'
            return u'【%s】%s%s [推奨Lv%s]' % (quest_type_name, cleard, quest.name, quest.pick_level)
        return u''
    
    @property
    def mark(self):
        return Mark.get(self.mark_id)
    
    @property
    def mark_name(self):
        mark = self.mark
        
        field = FieldType.get(mark.field_type)
        if mark.hide_mark:
            return u'%s [%s]【隠しマーク】' % (mark.name, field)
        else:
            return u'%s [%s]' % (mark.name, field)
    
    @property
    def pcmd_add_1_ch(self):
        return Character.get(self.pcm_add_1)
    
    @property
    def pcmd_add_2_ch(self):
        return Character.get(self.pcm_add_2)
    
    @property
    def pcmd_add_3_ch(self):
        return Character.get(self.pcm_add_3)
    
    @property
    def pcmd_add_4_ch(self):
        return Character.get(self.pcm_add_4)
    
    @property
    def pcmd_add_5_ch(self):
        return Character.get(self.pcm_add_5)
    
    @property
    def option_comes_no_ch(self):
        return Character.get(self.option_comes_no)
    
    @property
    def use_item_1_it(self):
        return CharacterHavingItem.get_chara_item(self.user, self.use_item_1)
    
    @property
    def use_item_2_it(self):
        return CharacterHavingItem.get_chara_item(self.user, self.use_item_2)
    
    @property
    def use_item_3_it(self):
        return CharacterHavingItem.get_chara_item(self.user, self.use_item_3)
    
    @property
    def prv_skill(self):
        return Skill.get(self.getting_private_skill)


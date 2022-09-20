# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import CachedBaseModel

from module.common.constant import CommonConstant
from module.master.quest.constant import QuerstConstant

from module.character.models import CharacterKeyItem, CharacterBattle, CharacterQuest, CharacterInstall, CharacterMovingMark,\
    Character
from module.regist.constant import RegistConstant

class Quest(CachedBaseModel):
    id = models.IntegerField(u'ID', primary_key=True)
    name = models.CharField(u'名称', max_length=100)
    client = models.CharField(u'依頼者', max_length=80, blank=True)
    quest_type = models.IntegerField(u'種別', choices=QuerstConstant.QUEST_TYPES, default=QuerstConstant.QUEST_TYPE_QUEST)
    pick_level = models.IntegerField(u'推奨レベル', default=1)
    keyitem_id = models.IntegerField(u'貴重品', default=0)
    offer_quest_id = models.IntegerField(u'受注済みクエスト', default=0)
    comp_quest_id = models.IntegerField(u'達成済みクエスト', default=0)
    sp_level = models.IntegerField(u'最低SP', default=0)
    install_class_id = models.IntegerField(u'必要クラス', default=0)
    class_level = models.IntegerField(u'必要クラス最低レベル', default=0)
    bc_level = models.IntegerField(u'必要BC', default=0)
    hide_fg = models.BooleanField(u'隠しクエスト？', default=False)

    class Meta:
        verbose_name = u'クエスト'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(Quest, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Quest, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_chices_list_cache_key(cls, user_id):
        return '%s/get_chices_list/%s' % (cls._meta, user_id)

    @classmethod
    def get_chices_list(cls, user):
        cache_key =  cls._get_get_chices_list_cache_key(user.id)

        l = cache.get(cache_key, [])
        if l:
            return l
        
        key_item_ids = CharacterKeyItem.get_chices_list(user)
        key_item_ids.append(0)
        
        offer_quest_ids = CharacterQuest.get_chices_list(user, 0)
        offer_quest_ids.append(0)
        complete_quest_ids = CharacterQuest.get_chices_list(user, 1)
        complete_quest_ids.append(0)
        
        chara_data = Character.get(user.id)
        bc_level = 0
        if chara_data:
            bc_level = chara_data.blaze_chip
        
        battle_data = CharacterBattle.get(user.id)
        sp_level = 1
        if battle_data:
            sp_level = battle_data.level
        
        class_data = CharacterInstall.get_install_dic(user)
        

        try:
            quests = cls.objects.filter(models.Q(hide_fg=False) |
                                    (models.Q(hide_fg=True) &
                                     models.Q(keyitem_id__in=key_item_ids) &
                                     models.Q(offer_quest_id__in=offer_quest_ids) &
                                     models.Q(comp_quest_id__in=complete_quest_ids) &
                                     models.Q(sp_level__lte=sp_level) &
                                     models.Q(bc_level__lte=bc_level))).order_by('id')
            quests = list(quests)
            
            l = []
            for quest in quests:
                if quest.install_class_id > 0 and quest.class_level > 0:
                    if class_data[quest.install_class_id] < quest.class_level:
                        continue
                
                is_bounty = False
                quest_type_name = u'クエスト'
                if quest.quest_type == QuerstConstant.QUEST_TYPE_MISSION:
                    quest_type_name = u'ミッション'
                elif quest.quest_type == QuerstConstant.QUEST_TYPE_EVENT:
                    quest_type_name = u'イベント'
                elif quest.quest_type == QuerstConstant.QUEST_TYPE_BOUNTY:
                    quest_type_name = u'バウンティ'
                    is_bounty = True
                if quest.id == 0:
                    l.append((quest.id, u'%s' % quest.name))
                else:
                    cleard = u''
                    if quest.id in complete_quest_ids:
                        cleard = u'《済》'
                    bounty_node = u''
                    if is_bounty:
                        bounty_node = u' [必要BC:%s]' % quest.bc_level
                    l.append((quest.id, u'【%s】%s%s [推奨Lv%s]%s' % (quest_type_name, cleard, quest.name, quest.pick_level, bounty_node)))
            
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class Mark(CachedBaseModel):
    quest = models.ForeignKey(Quest, verbose_name=u'クエスト')
    name = models.CharField(u'名称', max_length=100)
    field_type = models.IntegerField(u'フィールドタイプ', default=0)
    hide_mark = models.BooleanField(u'隠しマーク', default=False)

    class Meta:
        verbose_name = u'マーク'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(Mark, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Mark, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_chices_list_cache_key(cls, quest_id, user_id):
        return '%s/get_chices_list/%s/%s' % (cls._meta, quest_id, user_id)

    @classmethod
    def get_chices_list(cls, quest_id, user):
        if quest_id == 0:
            return [(0, u'メンバーの指定した場所へ向かいます')]
        
        cache_key =  cls._get_get_chices_list_cache_key(quest_id, user.id)

        l = cache.get(cache_key, [])
        if l:
            return l
        
        moving_mark_ids = CharacterMovingMark.get_chices_list(user)

        try:
            l = cls.objects.filter(models.Q(quest=quest_id) &
                                   (models.Q(hide_mark=False) |
                                    (models.Q(hide_mark=True) &
                                     models.Q(id__in=moving_mark_ids)))).order_by('id')
            marks = list(l)
            
            l = []
            for mark in marks:
                field = FieldType.get(mark.field_type)
                weathers = MarkWeather.get_mark_weather(mark.id)
                if mark.hide_mark:
                    l.append((mark.id, u'%s [%s]-[%s]【隠しマーク】' % (mark.name, field.name, weathers[0].weather_name)))
                else:
                    l.append((mark.id, u'%s [%s]-[%s]' % (mark.name, field.name, weathers[0].weather_name)))
                    
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class FieldType(CachedBaseModel):
    name = models.CharField(u'名称', max_length=100)

    class Meta:
        verbose_name = u'フィールドタイプ'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

class Weather(CachedBaseModel):
    name = models.CharField(u'名称', max_length=100)

    class Meta:
        verbose_name = u'天候'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

class MarkWeather(CachedBaseModel):
    mark = models.ForeignKey(Mark, verbose_name=u'マーク', db_index=True)
    count = models.IntegerField(u'更新回数', default=0, db_index=True)
    weather = models.ForeignKey(Weather, verbose_name=u'天候')

    class Meta:
        verbose_name = u'マーク天候'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '%s: %s' % (self.mark.name, self.count)
    
    
    @classmethod
    def _get_mark_weather_cache_key(cls, mark_id):
        return '%s/get_mark_weather/%s' % (cls._meta, mark_id)

    @classmethod
    def get_mark_weather(cls, mark_id):
        cache_key =  cls._get_mark_weather_cache_key(mark_id)

        l = cache.get(cache_key, [])
        if l:
            return l
        

        try:
            l = cls.objects.filter(mark=mark_id).order_by('count')
            l = list(l)
            
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l
    
    @property
    def weather_name(self):
        return Weather.get(self.weather_id).name




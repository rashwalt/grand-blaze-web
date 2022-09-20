# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.common.constant import CommonConstant

from module.abstract.cachedmodels.models import CachedBaseModel, MultiCharacterCachedModel

class Skill(CachedBaseModel):
    name = models.CharField(u'名称', max_length=200)
    sk_mp = models.IntegerField(u'消費MP', default=0)
    sk_tp = models.IntegerField(u'消費TP', default=0)
    sk_power = models.DecimalField(u'威力', max_digits=8, decimal_places=4, default=0)
    sk_damage_rate = models.DecimalField(u'ダメージ係数', max_digits=8, decimal_places=4, default=0)
    sk_plus_score = models.IntegerField(u'追加スコア', default=0)
    sk_hit = models.IntegerField(u'命中性能', default=0)
    sk_critical = models.IntegerField(u'クリティカル性能', default=0)
    sk_critical_type = models.IntegerField(u'クリティカルタイプ', default=0)
    sk_round = models.IntegerField(u'攻撃回数', default=0)
    sk_range = models.IntegerField(u'射程', default=0)
    sk_charge = models.IntegerField(u'チャージタイム', default=0)
    sk_hate = models.IntegerField(u'増加ヘイト', default=0)
    sk_vhate = models.IntegerField(u'回復ヘイト', default=0)
    sk_dhate = models.IntegerField(u'減少ヘイト', default=0)
    sk_antiair = models.BooleanField(u'対空効果', default=False)
    sk_target_restrict = models.IntegerField(u'指定ターゲット効果', default=0)
    sk_use_limit = models.IntegerField(u'使用条件', default=0)
    sk_fire = models.IntegerField(u'火', default=0)
    sk_freeze = models.IntegerField(u'氷', default=0)
    sk_air = models.IntegerField(u'風', default=0)
    sk_earth = models.IntegerField(u'土', default=0)
    sk_water = models.IntegerField(u'水', default=0)
    sk_thunder = models.IntegerField(u'雷', default=0)
    sk_holy = models.IntegerField(u'光', default=0)
    sk_dark = models.IntegerField(u'闇', default=0)
    sk_slash = models.IntegerField(u'斬', default=0)
    sk_pierce = models.IntegerField(u'突', default=0)
    sk_strike = models.IntegerField(u'打', default=0)
    sk_break = models.IntegerField(u'壊', default=0)
    sk_effect = models.TextField(u'エフェクト', blank=True)
    sk_type = models.IntegerField(u'種類', default=0, choices=CommonConstant.SKILL_TYPES)
    sk_atype = models.IntegerField(u'攻撃種別', default=0)
    sk_damage_type = models.IntegerField(u'ダメージ種別', default=0)
    sk_target_area = models.IntegerField(u'ターゲット範囲', default=0)
    sk_comment = models.TextField(u'解説文', blank=True)
    sk_target_party = models.IntegerField(u'ターゲットパーティ', default=0)
    sk_arts_category = models.IntegerField(u'アーツカテゴリー', default=0)

    class Meta:
        verbose_name = u'スキル'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(Skill, self).save(*args, **kwargs)
        cache.delete(self._get_get_list_by_type_cache_key(self.sk_arts_category))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_list_by_type_cache_key(self.sk_arts_category))
        super(Skill, self).delete(*args, **kwargs)
        
    @property
    def skill_category(self):
        return SkillCategory.get(self.sk_arts_category)

    @classmethod
    def _get_get_list_by_type_cache_key(cls, category_id):
        return '%s/get_list_by_type/%s' % (cls._meta, category_id)

    @classmethod
    def get_list_by_type(cls, category_id):
        cache_key =  cls._get_get_list_by_type_cache_key(category_id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(sk_arts_category=category_id).order_by('id')
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class SkillGet(MultiCharacterCachedModel):
    skill_id = models.IntegerField(u'スキル', default=0)

    class Meta:
        verbose_name = u'個人習得可能スキル'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(SkillGet, self).save(*args, **kwargs)
        cache.delete(self._get_get_skill_id_list_cache_key(self.user_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_skill_id_list_cache_key(self.user_id))
        super(SkillGet, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_skill_id_list_cache_key(cls, user_id):
        return '%s/get_skill_id_list/%s' % (cls._meta, user_id)

    @classmethod
    def get_skill_id_list(cls, user):
        cache_key =  cls._get_get_skill_id_list_cache_key(user.id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(user=user).values_list('skill_id', flat=True)
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class SkillGetList(CachedBaseModel):
    tm_level = models.IntegerField(u'習得レベル', default=0)
    tm_race = models.IntegerField(u'習得種族', default=0)
    condition_text = models.TextField(u'条件文章')
    skill = models.ForeignKey(Skill, verbose_name=u'スキル')

    class Meta:
        verbose_name = u'プライベートスキル'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.skill.name

    def save(self, *args, **kwargs):
        super(SkillGetList, self).save(*args, **kwargs)
        cache.delete(self._get_get_sorted_level_list_cache_key())

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_sorted_level_list_cache_key())
        super(SkillGetList, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_sorted_level_list_cache_key(cls):
        return '%s/get_sorted_level_list' % (cls._meta)

    @classmethod
    def get_sorted_level_list(cls):
        cache_key =  cls._get_get_sorted_level_list_cache_key()

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.all().select_related(depth=1).order_by('tm_level', 'id')
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l
    
    @property
    def cached_skill(self):
        return Skill.get(self.skill_id)
    
    @property
    def skill_name(self):
        return Skill.get(self.skill_id).name
    
    @property
    def skill_comment(self):
        return Skill.get(self.skill_id).sk_comment

class SkillCategory(CachedBaseModel):
    name = models.CharField(u'名称', max_length=100)
    type_id = models.IntegerField(u'テック', default=0)

    class Meta:
        verbose_name = u'スキルカテゴリ'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(SkillCategory, self).save(*args, **kwargs)
        cache.delete(self._get_get_chices_list_cache_key())

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_chices_list_cache_key())
        super(SkillCategory, self).delete(*args, **kwargs)
    
    
        




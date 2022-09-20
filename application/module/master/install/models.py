# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import CachedBaseModel

from module.master.skill.models import Skill

from module.common.constant import CommonConstant

class Install(CachedBaseModel):
    name = models.CharField(u'名称', max_length=100)
    up_hp = models.IntegerField(u'HP成長ランク', choices=CommonConstant.GROWUPS, default=CommonConstant.GROWUP_G)
    up_mp = models.IntegerField(u'MP成長ランク', choices=CommonConstant.GROWUPS, default=CommonConstant.GROWUP_G)
    up_str = models.IntegerField(u'力成長ランク', choices=CommonConstant.GROWUPS, default=CommonConstant.GROWUP_G)
    up_agi = models.IntegerField(u'敏捷成長ランク', choices=CommonConstant.GROWUPS, default=CommonConstant.GROWUP_G)
    up_mag = models.IntegerField(u'魔力成長ランク', choices=CommonConstant.GROWUPS, default=CommonConstant.GROWUP_G)
    up_unq = models.IntegerField(u'固有成長ランク', choices=CommonConstant.GROWUPS, default=CommonConstant.GROWUP_G)
    comment = models.TextField(u'コメント')

    class Meta:
        verbose_name = u'クラス'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(Install, self).save(*args, **kwargs)
        cache.delete(self._get_get_chices_list_cache_key())

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_chices_list_cache_key())
        super(Install, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_chices_list_cache_key(cls):
        return '%s/get_chices_list' % (cls._meta)

    @classmethod
    def get_chices_list(cls):
        cache_key =  cls._get_get_chices_list_cache_key()

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.all().values_list('id', 'name')
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class InstallSkill(CachedBaseModel):
    install = models.ForeignKey(Install, verbose_name=u'インストール', db_index=True)
    level = models.IntegerField(u'習得レベル', default=0)
    skill = models.ForeignKey(Skill, verbose_name=u'スキル')
    only_mode = models.IntegerField(u'使用制限', choices=CommonConstant.SKILL_ONLY_MODES, default=CommonConstant.SKILL_ONLY_MODE_ALWAYS)

    class Meta:
        verbose_name = u'クラススキル'
        verbose_name_plural = verbose_name
        unique_together = (('install','level','skill'),)

    def __unicode__(self):
        return  self.name

    def save(self, *args, **kwargs):
        super(InstallSkill, self).save(*args, **kwargs)
        cache.delete(self._get_get_list_by_under_cache_key(self.install_id, self.level))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_list_by_under_cache_key(self.install_id, self.level))
        super(InstallSkill, self).delete(*args, **kwargs)
        
    @property
    def skill_d(self):
        return Skill.get(self.skill_id)

    @classmethod
    def _get_get_list_by_under_cache_key(cls, install_id, level):
        return '%s/get_list_by_under/%s/%s' % (cls._meta, install_id, level)

    @classmethod
    def get_list_by_under(cls, install_id, level):
        cache_key =  cls._get_get_list_by_under_cache_key(install_id, level)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            skills = cls.objects.filter(install=install_id, level__lte=level)
            skills = list(skills)
            l = []
            for skill_data in skills:
                l.append(skill_data.skill_d)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

    @classmethod
    def _get_get_list_cache_key(cls, install_id):
        return '%s/get_list_da/%s' % (cls._meta, install_id)

    @classmethod
    def get_list(cls, install_id):
        cache_key =  cls._get_get_list_cache_key(install_id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(install=install_id, level__lte=50).order_by('level')
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l
        
    

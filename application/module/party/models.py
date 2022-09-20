# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import CachedBaseModel, CharacterCachedModel

from module.regist.constant import RegistConstant

from module.character.models import Character

class Party(CachedBaseModel):
    name = models.CharField(u'パーティ名', max_length=200)
    mark_id = models.IntegerField(u'マークID', null=True, blank=True)

    class Meta:
        verbose_name = u'パーティ情報'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: Party: %s' % (self.id, self.name)

class PartyBelong(CharacterCachedModel):
    party = models.ForeignKey(Party, verbose_name=u'パーティ')
    reader = models.BooleanField(u'リーダー', default=False)
    mark_id = models.IntegerField(u'マークID', null=True, blank=True)

    class Meta:
        verbose_name = u'パーティメンバー情報'
        verbose_name_plural = verbose_name
        unique_together = (('user','party'),)

    def __unicode__(self):
        return  '%s: PartyBelong: %s' % (self.party_id, self.user_id)

    def save(self, *args, **kwargs):
        super(PartyBelong, self).save(*args, **kwargs)
        cache.delete(self._get_filter_cache_key(self.user_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_filter_cache_key(self.user_id))
        super(PartyBelong, self).delete(*args, **kwargs)

    @classmethod
    def _get_filter_cache_key(cls, party_id):
        return '%s/FILTER/%s' % (cls._meta, party_id)

    @classmethod
    def get_filter_by_party_id(cls, party_id):
        cache_key = cls._get_filter_cache_key(party_id)

        l = cache.get(cache_key, None)

        if l:
            return l

        try:
            l = list(cls.objects.filter(party=party_id))
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

    @property
    def character(self):
        return Character.get(self.user_id)
    
    @property
    def party_d(self):
        return Party.get(self.party_id)

# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.core.cache import cache

from module.abstract.cachedmodels.models import CharacterCachedModel, MultiCharacterCachedModel

from module.regist.constant import RegistConstant

from module.master.item.models import Item
from module.master.skill.models import Skill

class Character(CharacterCachedModel):
    continue_cnt = models.IntegerField(u'継続回数', default=0)
    continue_bonus = models.IntegerField(u'継続ボーナス', default=0)
    account_status = models.IntegerField(u'アカウントステータス', default=0)
    new_play = models.IntegerField(u'新規参加者か', default=0)
    last_update = models.DateTimeField(u'最終更新日', default=datetime.datetime.now())
    new_gamer = models.IntegerField(u'新規登録時の更新回数', default=0)
    character_name = models.CharField(u'キャラクター名', max_length=250, blank=True)
    image_url = models.CharField(u'イメージURL', max_length=255, blank=True)
    image_width = models.IntegerField(u'イメージ横サイズ', null=True, blank=True)
    image_height = models.IntegerField(u'イメージ縦サイズ', null=True, blank=True)
    image_link_url = models.CharField(u'イメージリンクURL', max_length=255, blank=True)
    image_copyright = models.CharField(u'イメージ権利表記', max_length=180, blank=True)
    nick_name = models.CharField(u'愛称', max_length=80, default='')
    race_id = models.PositiveIntegerField(u'種族', default=1)
    guardian_id = models.PositiveIntegerField(u'守護者', default=RegistConstant.GUARDIAN_IGNIS)
    nation_id = models.IntegerField(u'所属国', default=0)
    have_money = models.IntegerField(u'所持金', default=0)
    blaze_chip = models.IntegerField(u'所持BC', default=0)
    age = models.IntegerField(u'年齢', default=0)
    sex = models.PositiveSmallIntegerField(u'性別', default=RegistConstant.SEX_UNKNOWN)
    max_item = models.IntegerField(u'最大所持アイテム数', default=50)
    max_bazzeritem = models.IntegerField(u'最大出品数', default=7)
    profile = models.TextField(u'プロフィール', blank=True)
    unique_name = models.CharField(u'ユニーク名', max_length=36, default='')
    height = models.IntegerField(u'身長', default=0)
    weight = models.IntegerField(u'体重', default=0)
    familiar_name = models.CharField(u'ファミリア名', max_length=80, blank=True)

    class Meta:
        verbose_name = u'キャラクター情報'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: Character: %s' % (self.user_id, self.character_name)

    @classmethod
    def get_search_article_list(cls, body):
        if body.isdigit():
            number = int(body)
        else:
            number = 0

        l = cls.objects.filter(models.Q(character_name__icontains=body)|models.Q(nick_name__icontains=body)|models.Q(user_id=number)).order_by('user')
        l = list(l)

        return l

class CharacterBattle(CharacterCachedModel):
    install = models.IntegerField(u'メインクラス', default=0)
    second_install = models.IntegerField(u'サブクラス', default=0)
    formation = models.IntegerField(u'隊列', default=RegistConstant.FORMATION_FOWARD, choices=RegistConstant.FORMATIONS)
    level = models.IntegerField(u'レベル', default=0)
    exp = models.IntegerField(u'経験値', default=0)
    hp = models.DecimalField(u'HP', max_digits=11, decimal_places=0, default=0)
    mp = models.DecimalField(u'MP', max_digits=11, decimal_places=0, default=0)
    exp_unit = models.IntegerField(u'獲得経験値', default=0)
    levelup_point = models.IntegerField(u'レベルアップポイント', default=0)

    class Meta:
        verbose_name = u'キャラクター戦闘能力'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: CharacterBattle' % (self.user_id)

class CharacterAction(MultiCharacterCachedModel):
    action_no = models.IntegerField(u'行動No', default=1, blank=True)
    action_target = models.IntegerField(u'バトルターゲット')
    action = models.IntegerField(u'バトルアクション', default=0)
    perks_id = models.IntegerField(u'スキルID', null=True, blank=True)

    class Meta:
        verbose_name = u'キャラクターバトルアクション'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: CharacterAction: %s' % (self.user_id, self.action_no)

    def save(self, *args, **kwargs):
        super(CharacterAction, self).save(*args, **kwargs)
        cache.delete(self._get_get_chices_list_cache_key(self.user_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_chices_list_cache_key(self.user_id))
        super(CharacterAction, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_chices_list_cache_key(cls, user_id):
        return '%s/get_chices_list/%s' % (cls._meta, user_id)

    @classmethod
    def get_chices_list(cls, user):
        cache_key =  cls._get_get_chices_list_cache_key(user.id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(user=user).values()
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l
    
class CharacterKeyItem(MultiCharacterCachedModel):
    keyitem_id = models.IntegerField(u'貴重品', default=0)

    class Meta:
        verbose_name = u'キャラクター貴重品'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: CharacterKeyItem: %s' % (self.user_id, self.keyitem_id)

    def save(self, *args, **kwargs):
        super(CharacterKeyItem, self).save(*args, **kwargs)
        cache.delete(self._get_get_chices_list_cache_key(self.user_id))
        cache.delete(self._get_get_unique_cache_key(self.user_id, self.keyitem_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_chices_list_cache_key(self.user_id))
        cache.delete(self._get_get_unique_cache_key(self.user_id, self.keyitem_id))
        super(CharacterKeyItem, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_chices_list_cache_key(cls, user_id):
        return '%s/get_chices_list/%s' % (cls._meta, user_id)

    @classmethod
    def get_chices_list(cls, user):
        cache_key =  cls._get_get_chices_list_cache_key(user.id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(user=user).values_list('keyitem_id', flat=True)
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

    @classmethod
    def _get_get_unique_cache_key(cls, user_id, keyitem_id):
        return '%s/get_unique/%s/%s' % (cls._meta, user_id, keyitem_id)

    @classmethod
    def get_unique(cls, user, keyitem_id):
        cache_key = cls._get_get_unique_cache_key(user.id, keyitem_id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.get(user=user, keyitem_id=keyitem_id)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class CharacterHavingSkill(MultiCharacterCachedModel):
    skill_id = models.IntegerField(u'スキル', default=0)
    is_new = models.BooleanField(u'新規獲得品か', default=False)
    sc_flg = models.BooleanField(u'スクロールフラグ', default=False)

    class Meta:
        verbose_name = u'キャラクター所持スキル'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: CharacterHavingSkill: %s' % (self.user_id, self.skill_id)

    def save(self, *args, **kwargs):
        super(CharacterHavingSkill, self).save(*args, **kwargs)
        cache.delete(self._get_get_skill_id_list_cache_key(self.user_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_skill_id_list_cache_key(self.user_id))
        super(CharacterHavingSkill, self).delete(*args, **kwargs)
        
    @property
    def skill(self):
        return Skill.get(self.skill_id)

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

class CharacterHavingItem(MultiCharacterCachedModel):
    box_type = models.IntegerField(u'ボックスタイプ', default=RegistConstant.BOX_TYPE_BAG, choices=RegistConstant.BOX_TYPES)
    have_no = models.IntegerField(u'所持番号', default=0)
    item_v = models.ForeignKey(Item, verbose_name=u'アイテム')
    it_box_count = models.IntegerField(u'所持数', default=0)
    it_box_baz_count = models.IntegerField(u'バザー出品数', default=0)
    equip_spot = models.IntegerField(u'装備位置', default=RegistConstant.EQUIP_SPOT_NONE, choices=RegistConstant.EQUIP_SPOTS)
    is_new = models.BooleanField(u'新規アイテム', default=False)
    created = models.BooleanField(u'作成品フラグ', default=False)
    it_name = models.CharField(u'アイテム名称', max_length=100, blank=True, null=True)
    it_comment = models.TextField(u'アイテム解説文', blank=True, null=True)
    it_effect = models.TextField(u'アイテム特殊効果', blank=True, null=True)
    it_price = models.DecimalField(u'購入価格', default=0, blank=True, null=True, max_digits=13, decimal_places=1)
    it_seller = models.DecimalField(u'売却価格', default=0, blank=True, null=True, max_digits=13, decimal_places=1)

    class Meta:
        verbose_name = u'キャラクター所持アイテム'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: CharacterHavingItem: %s' % (self.user_id, self.item_v_id)

    def save(self, *args, **kwargs):
        super(CharacterHavingItem, self).save(*args, **kwargs)
        cache.delete(self._get_get_chara_item_cache_key(self.user_id, self.item_v_id))
        cache.delete(self._get_get_filter_by_equipment_cache_key(self.user_id, RegistConstant.EQUIP_SPOT_MAIN))
        cache.delete(self._get_get_filter_by_haved_cache_key(self.user_id, self.have_no))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_chara_item_cache_key(self.user_id, self.item_v_id))
        cache.delete(self._get_get_filter_by_equipment_cache_key(self.user_id, RegistConstant.EQUIP_SPOT_MAIN))
        cache.delete(self._get_get_filter_by_haved_cache_key(self.user_id, self.have_no))
        super(CharacterHavingItem, self).delete(*args, **kwargs)
        
    @property
    def item(self):
        item_data = self.item_v
        if self.created:
            item_data.name = self.it_name
            item_data.it_comment = self.it_comment
            item_data.it_effect = self.it_effect
            item_data.it_price = self.it_price
            item_data.it_seller = self.it_seller
        return item_data

    @classmethod
    def _get_get_chara_item_cache_key(cls, user_id, item_id):
        return '%s/get_chara_item/%s/%s' % (cls._meta, user_id, item_id)

    @classmethod
    def get_chara_item(cls, user, item_id):
        cache_key = cls._get_get_chara_item_cache_key(user.id, item_id)

        v = cache.get(cache_key, None)
        if v:
            return v

        try:
            v = cls.objects.select_related(depth=1).get(user=user, have_no=item_id)
            cache.set(cache_key, v, 3600)
        except:
            v = None

        return v

    @classmethod
    def _get_get_filter_by_equipment_cache_key(cls, user_id, equip_id):
        return '%s/get_filter_by_equipment/%s/%s' % (cls._meta, user_id, equip_id)

    @classmethod
    def get_filter_by_equipment(cls, user, equip_id):
        cache_key = cls._get_get_filter_by_equipment_cache_key(user.id, equip_id)

        v = cache.get(cache_key, None)
        if v:
            return v

        try:
            v = cls.objects.get(user=user, box_type=RegistConstant.BOX_TYPE_BAG, equip_spot=equip_id)
            cache.set(cache_key, v, 3600)
        except:
            v = None

        return v

    @classmethod
    def _get_get_filter_by_haved_cache_key(cls, user_id, have_id):
        return '%s/get_filter_by_haved/%s/%s' % (cls._meta, user_id, have_id)

    @classmethod
    def get_filter_by_haved(cls, user, have_id):
        cache_key = cls._get_get_filter_by_haved_cache_key(user.id, have_id)

        v = cache.get(cache_key, None)
        if v:
            return v

        try:
            v = cls.objects.get(user=user, box_type=RegistConstant.BOX_TYPE_BAG, have_no=have_id)
            cache.set(cache_key, v, 3600)
        except:
            v = None

        return v

    @classmethod
    def get_filter_by_user(cls, user):
        cache_key = cls._get_filter_cache_key(user.id)

        l = cache.get(cache_key, None)

        if l:
            return l

        try:
            l = list(cls.objects.filter(user=user).select_related(depth=1))
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l
        


class CharacterQuest(MultiCharacterCachedModel):
    quest_id = models.IntegerField(u'クエスト', default=0)
    clear_fg = models.BooleanField(u'クリア済', default=False)
    step = models.IntegerField(u'クエスト進行度', default=0)

    class Meta:
        verbose_name = u'キャラクタークエスト'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: CharacterQuest: %s' % (self.user_id, self.keyitem_id)

    def save(self, *args, **kwargs):
        super(CharacterQuest, self).save(*args, **kwargs)
        cache.delete(self._get_get_chices_list_cache_key(self.user_id, 1))
        cache.delete(self._get_get_chices_list_cache_key(self.user_id, 0))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_chices_list_cache_key(self.user_id, 1))
        cache.delete(self._get_get_chices_list_cache_key(self.user_id, 0))
        super(CharacterQuest, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_chices_list_cache_key(cls, user_id, clear_flag):
        return '%s/get_chices_list/%s/%s' % (cls._meta, user_id, clear_flag)

    @classmethod
    def get_chices_list(cls, user, clear_flag):
        cache_key =  cls._get_get_chices_list_cache_key(user.id, clear_flag)

        l = cache.get(cache_key, [])
        if l:
            return l

        l = cls.objects.filter(user=user, clear_fg=clear_flag).values_list('quest_id', flat=True)
        l = list(l)
        cache.set(cache_key, l, 3600)

        return l

class CharacterInstall(MultiCharacterCachedModel):
    install_id = models.IntegerField(u'クラス', default=0)
    level = models.IntegerField(u'レベル', default=0)
    exp = models.IntegerField(u'経験値', default=0)

    class Meta:
        verbose_name = u'キャラクタークラス'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: CharacterInstall: %s' % (self.user_id, self.keyitem_id)

    def save(self, *args, **kwargs):
        super(CharacterInstall, self).save(*args, **kwargs)
        cache.delete(self._get_get_install_dic_cache_key(self.user_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_install_dic_cache_key(self.user_id))
        super(CharacterInstall, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_install_dic_cache_key(cls, user_id):
        return '%s/get_install_dic/%s' % (cls._meta, user_id)

    @classmethod
    def get_install_dic(cls, user):
        cache_key =  cls._get_get_install_dic_cache_key(user.id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            installs = cls.objects.filter(user=user)
            installs = list(installs)
            l = {}
            for install in installs:
                l[install.install_id] = install.level
            
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

    @classmethod
    def _get_get_install_cache_key(cls, user_id, install_id):
        return '%s/get_install_dic/%s/%s' % (cls._meta, user_id, install_id)

    @classmethod
    def get_install(cls, user, install_id):
        cache_key =  cls._get_get_install_cache_key(user.id, install_id)

        v = cache.get(cache_key, None)
        if v:
            return v

        try:
            v = cls.objects.get(user=user, install_id=install_id)
            cache.set(cache_key, v, 3600)
        except:
            pass

        return v
    
class CharacterMovingMark(MultiCharacterCachedModel):
    mark_id = models.IntegerField(u'マーク', default=0)
    instance = models.BooleanField(u'達成済か', default=False)

    class Meta:
        verbose_name = u'キャラクター移動可能マーク'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: CharacterMovingMark: %s' % (self.user_id, self.keyitem_id)

    def save(self, *args, **kwargs):
        super(CharacterMovingMark, self).save(*args, **kwargs)
        cache.delete(self._get_get_chices_list_cache_key(self.user_id))

    def delete(self, *args, **kwargs):
        super(CharacterMovingMark, self).delete(*args, **kwargs)
        cache.delete(self._get_get_chices_list_cache_key(self.user_id))

    @classmethod
    def _get_get_chices_list_cache_key(cls, user_id):
        return '%s/get_chices_list/%s' % (cls._meta, user_id)

    @classmethod
    def get_chices_list(cls, user):
        cache_key =  cls._get_get_chices_list_cache_key(user.id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(user=user).values_list('mark_id', flat=True)
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class CharacterIcon(MultiCharacterCachedModel):
    icon_id = models.IntegerField(u'アイコンNo', default=1, blank=True)
    icon_url = models.CharField(u'アイコンURL', max_length=255)
    icon_copyright = models.CharField(u'アイコン著作者', max_length=180)

    class Meta:
        verbose_name = u'キャラクターアイコン'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: CharacterIcon: %s' % (self.user_id, self.action_no)

    def save(self, *args, **kwargs):
        super(CharacterIcon, self).save(*args, **kwargs)
        cache.delete(self._get_get_chices_list_cache_key(self.user_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_chices_list_cache_key(self.user_id))
        super(CharacterIcon, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_chices_list_cache_key(cls, user_id):
        return '%s/get_chices_list/%s' % (cls._meta, user_id)

    @classmethod
    def get_chices_list(cls, user):
        cache_key =  cls._get_get_chices_list_cache_key(user.id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(user=user).values()
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l

class CharacterSerif(MultiCharacterCachedModel):
    word_no = models.IntegerField(u'セリフNo', default=1, blank=True)
    situation_id = models.IntegerField(u'シチュエーション')
    serif_text = models.TextField(u'セリフ内容')
    perks_id = models.IntegerField(u'スキルID', null=True, blank=True)

    class Meta:
        verbose_name = u'キャラクターセリフ'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  '%s: CharacterSerif: %s' % (self.user_id, self.action_no)

    def save(self, *args, **kwargs):
        super(CharacterSerif, self).save(*args, **kwargs)
        cache.delete(self._get_get_chices_list_cache_key(self.user_id))

    def delete(self, *args, **kwargs):
        cache.delete(self._get_get_chices_list_cache_key(self.user_id))
        super(CharacterSerif, self).delete(*args, **kwargs)

    @classmethod
    def _get_get_chices_list_cache_key(cls, user_id):
        return '%s/get_chices_list/%s' % (cls._meta, user_id)

    @classmethod
    def get_chices_list(cls, user):
        cache_key =  cls._get_get_chices_list_cache_key(user.id)

        l = cache.get(cache_key, [])
        if l:
            return l

        try:
            l = cls.objects.filter(user=user).order_by('situation_id', 'id').values()
            l = list(l)
            cache.set(cache_key, l, 3600)
        except:
            pass

        return l
    





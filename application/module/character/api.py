# -*- coding: utf-8 -*-

from module.character.models import Character, CharacterBattle, CharacterAction, CharacterHavingItem, CharacterHavingSkill, CharacterInstall, CharacterKeyItem, CharacterIcon, CharacterSerif
from module.regist.newgame.models import NewGame

from module.regist.constant import RegistConstant
from module.regist.continue_equip.api import ContinueEquipAPI

from module.master.install.api import InstallAPI
from module.common.constant import CommonConstant

class CharacterAPI(object):

    @classmethod
    def get(cls, user):
        if user.is_authenticated:
            return Character.get(user.id)
        else:
            return None
    
    @classmethod
    def search(cls, request, cleaned_data):
        body = cleaned_data['body']

        return Character.get_search_article_list(body)

class CharacterBattleAPI(object):

    @classmethod
    def get(cls, user):
        if user.is_authenticated:
            return CharacterBattle.get(user.id)
        else:
            return None

class CharacterActionAPI(object):

    @classmethod
    def get_chices_list(cls, user):
        if user.is_authenticated:
            choice_list = []
            for icon_row in CharacterAction.get_chices_list(user):
                choice_list.append({
                                    'action_target': icon_row['action_target'],
                                    'perks_id': icon_row['perks_id'],
                                    'action': icon_row['action'],
                                    })
            
            return choice_list
        else:
            return None

class CharacterKeyItemAPI(object):
    
    @classmethod
    def get_keyitem(cls, user, keyitem_id):
        return CharacterKeyItem.get_unique(user, keyitem_id)

class CharacterHaveItemAPI(object):

    @classmethod
    def get_filter(cls, user):
        if user.is_authenticated:
            return CharacterHavingItem.get_filter_by_user(user)
        else:
            return None

    @classmethod
    def get_filter_by_equipment(cls, user, equip_id):
        if user.is_authenticated:
            return CharacterHavingItem.get_filter_by_equipment(user, equip_id)
        else:
            return None

    @classmethod
    def get_filter_by_haved(cls, user, have_id):
        if user.is_authenticated:
            return CharacterHavingItem.get_filter_by_haved(user, have_id)
        else:
            return None

class CharacterInstallAPI(object):

    @classmethod
    def get(cls, user, install_id):
        if user.is_authenticated:
            return CharacterInstall.get_install(user, install_id)
        else:
            return None

class CharacterHaveSkillAPI(object):
    
    @classmethod
    def get_filter(cls, user):
        if user.is_authenticated:
            return CharacterHavingSkill.get_filter_by_user(user)
        else:
            return None

    @classmethod
    def get_using(cls, user):
        if user.is_authenticated:
            character_battle = CharacterBattleAPI.get(user)
            
            # クラスで使用可能なもの
            continue_equip = ContinueEquipAPI.get(user.id)
            
            install_id = 0
            if continue_equip and continue_equip.install > 0:
                install_id = continue_equip.install
            else:
                # 現在のインストール
                if character_battle:
                    install_id = character_battle.install
                else:
                    newgame = NewGame.get(user.id)
                    if newgame:
                        install_id = newgame.install_class_id
                    else:
                        install_id = 1
                
            # クラスのレベル取得
            install_data = CharacterInstallAPI.get(user, install_id)
            
            install_level = 1
            if install_data:
                install_level = install_data.level
            
            install_tmp_arts = InstallAPI.get_under_install(install_id, install_level)
            
            install_arts = []
            for install_tmp in install_tmp_arts:
                if install_tmp.sk_type != CommonConstant.SKILL_TYPE_ARTS and install_tmp.sk_type != CommonConstant.SKILL_TYPE_SPECIAL:
                    continue
                install_arts.append(install_tmp)
                
            # サブクラスで使用可能なもの
            sub_install_id = 0
            if continue_equip and continue_equip.secondary_install > 0:
                sub_install_id = continue_equip.secondary_install
            else:
                # 現在のインストール
                if character_battle:
                    sub_install_id = character_battle.second_install
            
            if sub_install_id:
                # クラスのレベル取得
                install_data = CharacterInstallAPI.get(user, sub_install_id)
                
                sub_install_level = 1
                if install_data:
                    sub_install_level = install_data.level
                    
                    if sub_install_level > int(install_level / 2):
                        sub_install_level = int(install_level / 2)
                
                install_tmp_arts = InstallAPI.get_under_install(sub_install_id, sub_install_level)
                
                for install_tmp in install_tmp_arts:
                    if install_tmp.sk_type != CommonConstant.SKILL_TYPE_ARTS:
                        continue
                    install_arts.append(install_tmp)
            
            # 装備武器による判定
            having_items = CharacterHaveItemAPI.get_filter_by_equipment(user, RegistConstant.EQUIP_SPOT_MAIN)
            
            main_weapon = None
            if continue_equip and continue_equip.equip_main > 0:
                having_items = CharacterHaveItemAPI.get_filter_by_haved(user, continue_equip.equip_main)
                if having_items:
                    main_weapon = having_items.item
            elif having_items:
                main_weapon = having_items.item
            
            # デフォルトは格闘
            tec_id = 1
            
            if main_weapon:
                item_type = main_weapon.item_type
                
                if item_type:
                    tec_id = item_type.skill_id
            
            # 所持スキル
            have_temp_arts = CharacterHaveSkillAPI.get_filter(user)
            have_arts = []
            
            if have_temp_arts:
                for have_art in have_temp_arts:
                    if have_art.skill.sk_type != CommonConstant.SKILL_TYPE_ARTS:
                        continue
                    if have_art.skill.skill_category and have_art.skill.skill_category.type_id > 0 and have_art.skill.skill_category.type_id != tec_id:
                        continue
                    have_arts.append(have_art.skill)
                
                install_arts.extend(have_arts)
                
                install_arts = list(set(install_arts))
            
            install_arts.sort()
            return install_arts
        else:
            return None

class CharacterIconAPI(object):

    @classmethod
    def get_chices_list(cls, user):
        if user.is_authenticated:
            choice_list = []
            for icon_row in CharacterIcon.get_chices_list(user):
                choice_list.append({
                                    'icon_url': icon_row['icon_url'],
                                    'icon_copyright': icon_row['icon_copyright'],
                                    })
            
            return choice_list
        else:
            return None

class CharacterSerifAPI(object):

    @classmethod
    def get_chices_list(cls, user):
        if user.is_authenticated:
            choice_list = []
            for icon_row in CharacterSerif.get_chices_list(user):
                choice_list.append({
                                    'situation_id': icon_row['situation_id'],
                                    'perks_id': icon_row['perks_id'],
                                    'serif_text': icon_row['serif_text'],
                                    })
            
            return choice_list
        else:
            return None
        
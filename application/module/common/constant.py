# -*- coding: utf-8 -*-

class CommonConstant(object):
    GROWUP_G = 0
    GROWUP_F = 1
    GROWUP_E = 2
    GROWUP_D = 3
    GROWUP_C = 4
    GROWUP_B = 5
    GROWUP_A = 6
    GROWUPS = (
        (GROWUP_G, u'G'),
        (GROWUP_F, u'F'),
        (GROWUP_E, u'E'),
        (GROWUP_D, u'D'),
        (GROWUP_C, u'C'),
        (GROWUP_B, u'B'),
        (GROWUP_A, u'A'),
    )
    
    TARGET_TYPE_ENEMY = 0
    TARGET_TYPE_FRIEND = 1
    TARGET_TYPE_MINE = 2
    TARGET_TYPES = (
        (TARGET_TYPE_ENEMY, u'敵対象'),
        (TARGET_TYPE_FRIEND, u'味方対象'),
        (TARGET_TYPE_MINE, u'自分対象'),
    )
    
    SKILL_ONLY_MODE_ALWAYS = 0
    SKILL_ONLY_MODE_PRIMARY = 1
    SKILL_ONLY_MODE_SECONDARY = 2
    SKILL_ONLY_MODE_SCROLLUSING = 3
    SKILL_ONLY_MODE_USINGELEMENTAL = 4
    SKILL_ONLY_MODES = (
        (SKILL_ONLY_MODE_ALWAYS, u'いつでも'),
        (SKILL_ONLY_MODE_PRIMARY, u'メインインストール'),
        (SKILL_ONLY_MODE_SECONDARY, u'サブインストール'),
        (SKILL_ONLY_MODE_SCROLLUSING, u'スクロール使用後'),
        (SKILL_ONLY_MODE_USINGELEMENTAL, u'精霊契約'),
    )
    
    SKILL_TYPE_ARTS = 0
    SKILL_TYPE_SUPPORT = 1
    SKILL_TYPE_ASSIST = 2
    SKILL_TYPE_SPECIAL = 3
    SKILL_TYPES = (
        (SKILL_TYPE_ARTS, u'アーツ'),
        (SKILL_TYPE_SUPPORT, u'サポート'),
        (SKILL_TYPE_ASSIST, u'アシスト'),
        (SKILL_TYPE_SPECIAL, u'スペシャル'),
    )
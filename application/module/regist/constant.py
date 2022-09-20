# -*- coding: utf-8 -*-

class RegistConstant(object):
    SEX_UNKNOWN = 0
    SEX_MALE = 1
    SEX_FEMALE = 2
    SEXS = (
        (SEX_UNKNOWN, u'不明'),
        (SEX_MALE, u'男性'),
        (SEX_FEMALE, u'女性'),
    )
    
    GUARDIAN_IGNIS = 1
    GUARDIAN_CELSIUS = 2
    GUARDIAN_CHAFFLICCA = 3
    GUARDIAN_KTWELCCAN = 4
    GUARDIAN_KARSHACK = 5
    GUARDIAN_IVAN = 6
    GUARDIAN_ISHTAS = 7
    GUARDIAN_UNPLUTO = 8
    GUARDIANS = (
        (GUARDIAN_IGNIS, u'修羅の炎帝イグニート'),
        (GUARDIAN_CELSIUS, u'氷花の乙女セルシウス'),
        (GUARDIAN_CHAFFLICCA, u'風来の鬼神チャフリカ'),
        (GUARDIAN_KTWELCCAN, u'地獄の咆哮クツェルカン'),
        (GUARDIAN_KARSHACK, u'湧泉の真人カアシャック'),
        (GUARDIAN_IVAN, u'轟縛の雷帝イーヴァン'),
        (GUARDIAN_ISHTAS, u'閃光の翼士イシュタス'),
        (GUARDIAN_UNPLUTO, u'漆黒の魔手アン・プトゥ'),
    )
    
    WEAPON_HANDS = 1
    WEAPON_DAGGER = 2
    WEAPON_SWORD = 3
    WEAPON_AXE = 4
    WEAPON_KODACHI = 5
    WEAPON_WHIP = 6
    WEAPON_BOOK = 7
    WEAPON_MYST = 8
    WEAPON_GERATSWORD = 9
    WEAPON_KATANA = 10
    WEAPON_STAFF = 11
    WEAPON_SPEAR = 12
    WEAPON_POLE = 13
    WEAPON_MUSICAL = 14
    WEAPON_RANGE = 15
    WEAPON_BOW = 16
    WEAPON_BOWGUN = 17
    WEAPON_GUN = 18
    WEAPONS = (
        (WEAPON_HANDS, u'格闘'),
        (WEAPON_DAGGER, u'短剣'),
        (WEAPON_SWORD, u'片手剣'),
        (WEAPON_AXE, u'片手斧'),
        (WEAPON_KODACHI, u'片手刀'),
        (WEAPON_WHIP, u'片手鞭'),
        (WEAPON_BOOK, u'書物'),
        (WEAPON_MYST, u'魔導器'),
        (WEAPON_GERATSWORD, u'両手剣'),
        (WEAPON_KATANA, u'両手刀'),
        (WEAPON_STAFF, u'両手杖'),
        (WEAPON_SPEAR, u'両手槍'),
        (WEAPON_POLE, u'両手棒'),
        (WEAPON_MUSICAL, u'楽器'),
        (WEAPON_RANGE, u'投擲'),
        (WEAPON_BOW, u'弓'),
        (WEAPON_BOWGUN, u'弩'),
        (WEAPON_GUN, u'銃'),
    )
    
    NATION_FARNELD = 1
    NATION_WALD = 2
    NATION_NELLVALLIA = 3
    NATION_DANAKS = 4
    NATIONS = (
        (NATION_FARNELD, u'ファーネルド連邦'),
        (NATION_WALD, u'ワルド帝国'),
        (NATION_NELLVALLIA, u'ネルヴァリア王国'),
        (NATION_DANAKS, u'ダナクス諸侯連合'),
    )
    
    PARTY_HOPE_STAY = 0
    PARTY_HOPE_HOPE = 1
    PARTY_HOPE_RANDOM = 2
    PARTY_HOPE_FREEJOIN = 3
    PARTY_HOPES = (
        (PARTY_HOPE_STAY, u'現状を維持する'),
        (PARTY_HOPE_HOPE, u'パーティへの参加希望を出す'),
        (PARTY_HOPE_RANDOM, u'ランダムパーティに参加する'),
        (PARTY_HOPE_FREEJOIN, u'ランダムパーティから参加者を募る'),
    )
    
    PARTY_SECESSION_STAY = 0
    PARTY_SECESSION_REMOVE = 1
    PARTY_SECESSIONS = (
        (PARTY_SECESSION_STAY, u'現在のパーティで冒険を続ける'),
        (PARTY_SECESSION_REMOVE, u'現在のパーティから離脱する'),
    )
    
    FORMATION_STAY = 0
    FORMATION_FOWARD = 1
    FORMATION_BACKYARD = 2
    FORMATIONS = (
        (FORMATION_STAY, u'変更なし'),
        (FORMATION_FOWARD, u'前列'),
        (FORMATION_BACKYARD, u'後列'),
    )
    
    BOX_TYPE_BAG = 0
    BOX_TYPE_TEMPORARY = 1
    BOX_TYPES = (
        (BOX_TYPE_BAG, u'カバン'),
        (BOX_TYPE_TEMPORARY, u'テンポラリ'),
    )
    
    EQUIP_SPOT_NONE = 0
    EQUIP_SPOT_MAIN = 1
    EQUIP_SPOT_SUB = 2
    EQUIP_SPOT_HEAD = 3
    EQUIP_SPOT_BODY = 4
    EQUIP_SPOT_ACCESORY = 5
    EQUIP_SPOTS = (
        (EQUIP_SPOT_NONE, u'なし'),
        (EQUIP_SPOT_MAIN, u'メイン'),
        (EQUIP_SPOT_SUB, u'サブ'),
        (EQUIP_SPOT_HEAD, u'頭部'),
        (EQUIP_SPOT_BODY, u'胴体'),
        (EQUIP_SPOT_ACCESORY, u'装飾'),
    )
    
    SHOP_ACT_BUY = 0
    SHOP_ACT_SELL = 1
    SHOP_ACTS = (
        (SHOP_ACT_BUY, u'購入'),
        (SHOP_ACT_SELL, u'売却'),
    )
    
    ACCOUNT_STAT_ACTIVE = 0
    ACCOUNT_STAT_FREEZE = 1
    ACCOUNT_STAT_DELETE = 2
    ACCOUNT_STATUS = (
        (ACCOUNT_STAT_ACTIVE, u'アクティブ(初期状態)'),
        (ACCOUNT_STAT_FREEZE, u'フリーズ(凍結する)'),
        (ACCOUNT_STAT_DELETE, u'削除'),
    )
    
    MESSAGE_TARGET_PRIVATE = 0
    MESSAGE_TARGET_PARTY = 1
    MESSAGE_TARGET_LIST = 2
    MESSAGE_TARGETS = (
        (MESSAGE_TARGET_PRIVATE, u'個人宛て'),
        (MESSAGE_TARGET_PARTY, u'パーティメンバーに'),
        (MESSAGE_TARGET_LIST, u'リストに表示'),
    )
    
    
    
    
    
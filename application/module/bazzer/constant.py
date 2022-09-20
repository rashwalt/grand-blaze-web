# -*- coding: utf-8 -*-

class BazzerConstant(object):
    BAZZER_STATUS_SELL = 0
    BAZZER_STATUS_COMPLETE = 1
    BAZZER_STATUS_CLOSED = 2
    BAZZER_STATUS_CANCEL = 3
    BAZZER_STATUSES = (
        (BAZZER_STATUS_SELL, u'販売中'),
        (BAZZER_STATUS_COMPLETE, u'売り切れ'),
        (BAZZER_STATUS_CLOSED, u'時間超過による自動キャンセル'),
        (BAZZER_STATUS_CANCEL, u'キャンセル'),
    )
    
    SORT_ID = 0
    SORT_NAME = 1
    SORT_PRICE = 2
    SORT_PHYSICAL = 3
    SORT_MAGICAL = 4
    SORT_PHYSICAL_PARRY = 5
    SORT_MAGICAL_PARRY = 6
    SORT_LIST = (
        (SORT_ID, u'出品順'),
        (SORT_NAME, u'名前順'),
        (SORT_PRICE, u'価格順'),
        (SORT_PHYSICAL, u'物理性能順'),
        (SORT_MAGICAL, u'魔法性能順'),
        (SORT_PHYSICAL_PARRY, u'物理回避順'),
        (SORT_MAGICAL_PARRY, u'魔法回避順'),
    )
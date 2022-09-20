# -*- coding: utf-8 -*-

class QuerstConstant(object):
    
    QUEST_TYPE_QUEST = 0
    QUEST_TYPE_MISSION = 1
    QUEST_TYPE_BOUNTY = 9
    QUEST_TYPE_EVENT = 10
    QUEST_TYPES = (
        (QUEST_TYPE_QUEST, u'クエスト'),
        (QUEST_TYPE_MISSION, u'ミッション'),
        (QUEST_TYPE_BOUNTY, u'バウンティ'),
        (QUEST_TYPE_EVENT, u'イベント'),
    )

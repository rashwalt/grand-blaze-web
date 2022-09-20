# -*- coding: utf-8 -*-

class NoticeConstant(object):
    
    CATEGORY_IMPORTANT = 0
    CATEGORY_NORMAL = 1
    CATEGORY_VERSIONUP = 2
    CATEGORY_EVENT = 3
    CATEGORY_MAINTENANCE = 4
    CATEGORY_TOPICS = 5
    CATEGORYS = (
        (CATEGORY_IMPORTANT, u'重要なお知らせ'),
        (CATEGORY_NORMAL, u'一般情報'),
        (CATEGORY_VERSIONUP, u'バージョンアップ情報'),
        (CATEGORY_EVENT, u'イベント情報'),
        (CATEGORY_MAINTENANCE, u'メンテナンス情報'),
        (CATEGORY_TOPICS, u'トピックス'),
    )
    
    @classmethod
    def get_category_name(cls, category_id):
        for id, value in cls.CATEGORYS:
            if id == category_id:
                return value
        return None
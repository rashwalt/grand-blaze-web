# -*- coding: utf-8 -*-

class SupportConstant(object):
    
    SUBJECT_BUG = 0
    SUBJECT_REQUEST = 1
    SUBJECT_IDEA = 2
    SUBJECT_STF = 3
    SUBJECT_ALL = 4
    SUBJECTS = (
        (SUBJECT_BUG, u'バグ・誤字脱字の報告'),
        (SUBJECT_REQUEST, u'ご意見やご要望'),
        (SUBJECT_IDEA, u'システム、シナリオのアイデア投稿'),
        (SUBJECT_STF, u'不正行為の報告'),
        (SUBJECT_ALL, u'その他のお問い合わせ'),
    )
    
    @classmethod
    def get_subject_name(cls, subject_id):
        for id, value in cls.SUBJECTS:
            if id == subject_id:
                return value
        return None

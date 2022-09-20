# -*- coding: utf-8 -*-

import datetime

from django.core.cache import cache
from django.db.models import Q

from module.master.notice.models import Notice
from module.master.notice.constant import NoticeConstant

class NoticeAPI(object):
    
    @classmethod
    def get_top(cls, limit=5):
        
        return Notice.get_top(limit)
    
    @classmethod
    def get_active_category_top(cls, category, limit=5):
        
        return Notice.get_active_category_top(category, limit)
    
    @classmethod
    def get_category_top(cls, category, limit=5):
        return Notice.get_category_top(category, limit)
    
    @classmethod
    def get(cls, key_id):

        return Notice.get(key_id)

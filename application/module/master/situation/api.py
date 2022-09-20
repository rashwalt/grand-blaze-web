# -*- coding: utf-8 -*-

from module.master.situation.models import Situation

class SituationAPI(object):
    
    @classmethod
    def get_choices_list(cls):
        return Situation.get_chices_list()
    
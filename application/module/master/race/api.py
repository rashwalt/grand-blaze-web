# -*- coding: utf-8 -*-

from module.master.race.models import Race

class RaceAPI(object):
    
    @classmethod
    def get_choices_list(cls):
        return Race.get_chices_list()
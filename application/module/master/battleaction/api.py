# -*- coding: utf-8 -*-

from module.master.battleaction.models import BattleAction, BattleTarget

class BattleActionAPI(object):
    
    @classmethod
    def get_choices_list(cls):
        return BattleAction.get_chices_list()

class BattleTargetAPI(object):
    
    @classmethod
    def get_choices_list(cls):
        return BattleTarget.get_chices_list()
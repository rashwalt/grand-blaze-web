# -*- coding: utf-8 -*-

from module.master.quest.models import Quest, Mark, MarkWeather

from module.regist.newgame.models import NewGame

class QuestAPI(object):
    
    @classmethod
    def get_choices_list(cls, user):
        newgame = NewGame.get(user.id)
        if newgame:
            return ((0, u'【ミッション】ようこそギルドへ！ [推奨Lv1]'),)
        
        return Quest.get_chices_list(user)
    
    
class MarkAPI(object):
    
    @classmethod
    def get_choices_list(cls, quest_id, user):
        newgame = NewGame.get(user.id)
        if newgame:
            return ((1, u'はじまりの場所 [草地]-[晴れ]'),)
        
        return Mark.get_chices_list(quest_id, user)
    
    @classmethod
    def get_weather_list(cls, mark_list, user):
        newgame = NewGame.get(user.id)
        if newgame:
            return ((u'晴れ', u'晴れ', u'晴れ'),)
        
        weather_list = []
        for mark_id, mark_name in mark_list:
            weathers = MarkWeather.get_mark_weather(mark_id)
            weather_names = []
            for weather in weathers:
                weather_names.append(weather.weather_name)
            weather_list.append(weather_names)
        
        return weather_list
        
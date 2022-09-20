# -*- coding:utf-8 -*-

from django.conf import settings

from library.send_mail import send_mail

from module.regist.continue_complete.models import ContinueComplete
from module.regist.continue_main.api import ContinueMainAPI
from module.regist.continue_trade.api import ContinueTradeAPI
from module.regist.continue_battleaction.api import ContinueBattleActionAPI
from module.regist.continue_equip.api import ContinueEquipAPI
from module.regist.continue_profile.api import ContinueProfileAPI
from module.regist.continue_serif.api import ContinueSerifAPI
from module.regist.continue_message.api import ContinueMessageAPI
from module.regist.continue_icon.api import ContinueIconAPI
from module.regist.newgame.api import NewGameAPI
from module.character.api import CharacterAPI

class ConfirmAPI(object):
    
    @classmethod
    def send_mail(cls, request):
        user = request.user
        character = CharacterAPI.get(user)
        completed = ContinueComplete.get_categorys(user)
        
        subject = u"[Grand Blaze] : 登録内容のお知らせ"
        
        body = u"""
%s 様

Grand Blazeに登録された「各種登録」の内容です。

以下の情報で、登録されました。
登録内容をご確認ください。

Entry No: %s
キャラクター名: %s
""" % (user.email, user.id, character.character_name)

        body += NewGameAPI.get_mail(user)
        
        if 'continue' in completed:
            body += ContinueMainAPI.get_mail(user)
            
        if 'trade' in completed:
            body += ContinueTradeAPI.get_mail(user)
        
        if 'equip' in completed:
            body += ContinueEquipAPI.get_mail(user)
            
        if 'action' in completed:
            body += ContinueBattleActionAPI.get_mail(user)
            
        if 'account' in completed:
            body += ContinueProfileAPI.get_mail(user)
            
        if 'icon' in completed:
            body += ContinueIconAPI.get_mail(user)
            
        if 'message' in completed:
            body += ContinueMessageAPI.get_mail(user)
            
        if 'serif' in completed:
            body += ContinueSerifAPI.get_mail(user)
        
        body += u"""
--------------------------------------------------------------

本メールはGrand Blaze各種登録からの自動送信です。
身に覚えのない場合は、お手数ですが削除をお願いいたします。

-------------------------------------------------------------
Grand Blaze
http://www.grand-blaze.com/
-------------------------------------------------------------
"""
        send_mail(subject, body, settings.MAIL_FROM, [user.email])
        
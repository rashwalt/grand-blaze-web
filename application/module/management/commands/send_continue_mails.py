# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.management.base import BaseCommand

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
from module.character.api import CharacterAPI

from module.account.api import UserProfileAPI

class Command(BaseCommand):
    
    def handle(self, *args, **option):
        completes = ContinueComplete.get_last_entry()
        
        for complete in completes:
            lasted = ContinueComplete.get_last(complete['user'])
            
            if not lasted:
                continue
            
            user = UserProfileAPI.get_user(complete['user'])
            profile = UserProfileAPI.get_or_create_user_profile_by_user(user)
            
            character = CharacterAPI.get(user)
            
            if not profile.continue_mail:
                continue
            
            subject = u"[Grand Blaze] : 登録内容のお知らせ"
            
            body = u"""
%s 様

Grand Blazeに登録された「各種登録」の内容です。

以下の情報で、登録されました。
登録内容をご確認ください。

Entry No: %s
キャラクター名: %s
""" % (user.email, character.user_id, character.character_name)
            
            if 'continue' in lasted:
                body += ContinueMainAPI.get_mail(user)
                
            if 'trade' in lasted:
                body += ContinueTradeAPI.get_mail(user)
            
            if 'equip' in lasted:
                body += ContinueEquipAPI.get_mail(user)
                
            if 'action' in lasted:
                body += ContinueBattleActionAPI.get_mail(user)
                
            if 'account' in lasted:
                body += ContinueProfileAPI.get_mail(user)
                
            if 'icon' in lasted:
                body += ContinueIconAPI.get_mail(user)
                
            if 'message' in lasted:
                body += ContinueMessageAPI.get_mail(user)
                
            if 'serif' in lasted:
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
            
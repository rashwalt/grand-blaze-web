# -*- coding: utf-8 -*-

from django.template.loader import render_to_string

from module.character.models import Character
from module.regist.continue_complete.models import ContinueComplete
from module.regist.continue_main.models import ContinueMain

from module.regist.newgame.api import NewGameAPI

class ContinueMainAPI(object):
    
    @classmethod
    def get(cls, user_id):
        return ContinueMain.get(user_id)
    
    @classmethod
    def update_continue_main(cls, request, continue_main):
        user = request.user
        
        # 送信者情報
        ip_address = request.META.get('REMOTE_ADDR','')
        host = request.META.get('REMOTE_HOST', '')
        agent = request.META.get('HTTP_USER_AGENT','')
        
        # Continue Main save
        continue_main.user = user
        continue_main.ip_address = ip_address
        continue_main.host_address = host
        continue_main.user_agent = agent
        continue_main.save()
        
        # Continue Complete
        ContinueComplete.completed(user, 'continue', ip_address, host, agent)
    
    @classmethod
    def get_mail(cls, user):
        character = Character.get(user.id)
        
        continue_main = cls.get(user.id)
        
        ctxt = {
                'user_id': user.id,
                'character_name': character.character_name,
                'data': continue_main,
                'character': character,
                }
        
        return render_to_string('regist/continue_main/mail.html', ctxt)

        
        
        
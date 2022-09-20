# -*- coding: utf-8 -*-

from django.template.loader import render_to_string

from module.character.models import Character
from module.regist.continue_complete.models import ContinueComplete
from module.regist.continue_equip.models import ContinueEquip

class ContinueEquipAPI(object):
    
    @classmethod
    def get(cls, user_id):
        return ContinueEquip.get(user_id)
    
    @classmethod
    def update_continue_equip(cls, request, continue_equip, is_subset):
        user = request.user
        
        # 送信者情報
        ip_address = request.META.get('REMOTE_ADDR','')
        host = request.META.get('REMOTE_HOST', '')
        agent = request.META.get('HTTP_USER_AGENT','')
        
        # Continue Main save
        continue_equip.user = user
        continue_equip.ip_address = ip_address
        continue_equip.host_address = host
        continue_equip.user_agent = agent
        if not is_subset:
            continue_equip.secondary_install = 0
        continue_equip.save()
        
        # Continue Complete
        ContinueComplete.completed(user, 'equip', ip_address, host, agent)
    
    @classmethod
    def get_mail(cls, user):
        character = Character.get(user.id)
        
        continue_equip = cls.get(user.id)
        
        ctxt = {
                'user_id': user.id,
                'character_name': character.character_name,
                'data': continue_equip,
                }
        
        return render_to_string('regist/continue_equip/mail.html', ctxt)

        
        
        
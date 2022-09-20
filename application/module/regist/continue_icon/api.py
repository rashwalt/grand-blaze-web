# -*- coding: utf-8 -*-

from django.template.loader import render_to_string

from module.character.models import Character
from module.regist.continue_complete.models import ContinueComplete
from module.regist.continue_icon.models import ContinueIcon

class ContinueIconAPI(object):
    
    @classmethod
    def get(cls, user_id):
        return ContinueIcon.get_filter_by_user(user_id)
    
    @classmethod
    def get_query(cls, user_id):
        return ContinueIcon.objects.filter(user=user_id)
    
    @classmethod
    def update_continue_icon(cls, request, continue_icons):
        user = request.user
        
        # 送信者情報
        ip_address = request.META.get('REMOTE_ADDR','')
        host = request.META.get('REMOTE_HOST', '')
        agent = request.META.get('HTTP_USER_AGENT','')
        
        continue_icon_del_list = ContinueIcon.get_filter_by_user(user.id)
        for del_data in continue_icon_del_list:
            del_data.delete()
        
        # Continue Icon multi save
        number = 1
        for temp_data in continue_icons:
            ContinueIcon.objects.create(user=user, icon_id=number, icon_url=temp_data.icon_url, icon_copyright=temp_data.icon_copyright, ip_address=ip_address, host_address=host, user_agent=agent)
            number = number + 1
        
        # Continue Complete
        ContinueComplete.completed(user, 'icon', ip_address, host, agent)
    
    @classmethod
    def get_mail(cls, user):
        character = Character.get(user.id)
        
        continue_icons = cls.get(user.id)
        
        ctxt = {
                'user_id': user.id,
                'character_name': character.character_name,
                'datas': continue_icons,
                }
        
        return render_to_string('regist/continue_icon/mail.html', ctxt)
        
        
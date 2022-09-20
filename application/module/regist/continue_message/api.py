# -*- coding: utf-8 -*-

from django.template.loader import render_to_string

from module.character.models import Character
from module.regist.continue_complete.models import ContinueComplete
from module.regist.continue_message.models import ContinueMessage

class ContinueMessageAPI(object):
    
    @classmethod
    def get(cls, user_id):
        return ContinueMessage.get_filter_by_user(user_id)
    
    @classmethod
    def get_query(cls, user_id):
        return ContinueMessage.objects.filter(user=user_id)
    
    @classmethod
    def get_query_none(cls, user_id):
        return ContinueMessage.objects.filter(user=user_id).none()
    
    @classmethod
    def update_continue_message(cls, request, continue_messages):
        user = request.user
        
        # 送信者情報
        ip_address = request.META.get('REMOTE_ADDR','')
        host = request.META.get('REMOTE_HOST', '')
        agent = request.META.get('HTTP_USER_AGENT','')
        
        continue_message_del_list = ContinueMessage.get_filter_by_user(user.id)
        for del_data in continue_message_del_list:
            del_data.delete()
        
        # Continue Message multi save
        number = 1
        for temp_data in continue_messages:
            ContinueMessage.objects.create(user=user, mes_no=number, message_target=temp_data.message_target, message_entry=temp_data.message_entry, message_body=temp_data.message_body, ip_address=ip_address, host_address=host, user_agent=agent)
            number = number + 1
        
        # Continue Complete
        ContinueComplete.completed(user, 'message', ip_address, host, agent)
    
    @classmethod
    def get_mail(cls, user):
        character = Character.get(user.id)
        
        continue_messages = cls.get(user.id)
        
        ctxt = {
                'user_id': user.id,
                'character_name': character.character_name,
                'datas': continue_messages,
                }
        
        return render_to_string('regist/continue_message/mail.html', ctxt)

        
# -*- coding: utf-8 -*-

from django.template.loader import render_to_string

from module.character.models import Character
from module.regist.continue_complete.models import ContinueComplete
from module.regist.continue_profile.models import ContinueProfile

class ContinueProfileAPI(object):
    
    @classmethod
    def get(cls, user_id):
        return ContinueProfile.get(user_id)
    
    @classmethod
    def update_continue_profile(cls, request, continue_profile):
        user = request.user
        
        # 送信者情報
        ip_address = request.META.get('REMOTE_ADDR','')
        host = request.META.get('REMOTE_HOST', '')
        agent = request.META.get('HTTP_USER_AGENT','')
        
        # Continue Main save
        continue_profile.user = user
        continue_profile.ip_address = ip_address
        continue_profile.host_address = host
        continue_profile.user_agent = agent
        continue_profile.save()
        
        # Continue Complete
        ContinueComplete.completed(user, 'account', ip_address, host, agent)
    
    @classmethod
    def get_mail(cls, user):
        character = Character.get(user.id)
        
        continue_profile = cls.get(user.id)
        
        ctxt = {
                'user_id': user.id,
                'character_name': character.character_name,
                'data': continue_profile,
                }
        
        return render_to_string('regist/continue_profile/mail.html', ctxt)
    
    @classmethod
    def get_initial_data(cls, user):
        character = Character.get(user.id)
        
        initial_data = {}
        initial_data['nick_name'] = character.nick_name
        initial_data['age'] = character.age
        initial_data['height'] = character.height
        initial_data['weight'] = character.weight
        initial_data['profile'] = character.profile
        initial_data['image_url'] = character.image_url
        initial_data['image_width'] = character.image_width if character.image_width else u''
        initial_data['image_height'] = character.image_height if character.image_height else u''
        initial_data['image_link_url'] = character.image_link_url
        initial_data['image_copyright'] = character.image_copyright
        initial_data['unique_name'] = character.unique_name
        return initial_data

        
        
        
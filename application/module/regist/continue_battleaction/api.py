# -*- coding: utf-8 -*-

from django.template.loader import render_to_string
from django.core.cache import cache

from module.character.models import Character
from module.regist.continue_complete.models import ContinueComplete
from module.regist.continue_battleaction.models import ContinueBattleAction, SavingActionHead, SavingActionBody

class ContinueBattleActionAPI(object):
    
    @classmethod
    def get(cls, user_id):
        return ContinueBattleAction.get_filter_by_user(user_id)
    
    @classmethod
    def get_query(cls, user_id):
        return ContinueBattleAction.objects.filter(user=user_id)
    
    @classmethod
    def update_continue_battleaction(cls, request, continue_battleactions):
        user = request.user
        
        # 送信者情報
        ip_address = request.META.get('REMOTE_ADDR','')
        host = request.META.get('REMOTE_HOST', '')
        agent = request.META.get('HTTP_USER_AGENT','')
        
        continue_battleaction_del_list = ContinueBattleAction.get_filter_by_user(user.id)
        for del_data in continue_battleaction_del_list:
            del_data.delete()
        
        # Continue Battle Action multi save
        number = 1
        for temp_data in continue_battleactions:
            ContinueBattleAction.objects.create(user=user, action_no=number, action_target=temp_data.action_target, action=temp_data.action, perks_id=temp_data.perks_id, ip_address=ip_address, host_address=host, user_agent=agent)
            number = number + 1
        
        # Continue Complete
        ContinueComplete.completed(user, 'action', ip_address, host, agent)
    
    @classmethod
    def get_mail(cls, user):
        character = Character.get(user.id)
        
        continue_battleactions = cls.get(user.id)
        
        ctxt = {
                'user_id': user.id,
                'character_name': character.character_name,
                'datas': continue_battleactions,
                'user': user,
                }
        
        return render_to_string('regist/continue_battleaction/mail.html', ctxt)
        

class SavingActionAPI(object):
    
    @classmethod
    def get_head_list(cls, user):
        return SavingActionHead.get_filter_by_user_values(user)
    
    @classmethod
    def get_head(cls, saving_id):
        return SavingActionHead.get_values(saving_id)
    
    @classmethod
    def get_body(cls, saving_id):
        return SavingActionBody.get_unique_list(saving_id)
    
    @classmethod
    def update_saved_action(cls, request, formset, cleaned_data):
        title = cleaned_data['title']
        saving_id = cleaned_data['saving_id']
        
        head_list_count = SavingActionHead.objects.filter(user=request.user).exclude(name=title).count()
        
        if head_list_count >= 10:
            return True
        
        saving_head_list = SavingActionHead.objects.filter(user=request.user, name=title)
        created = False
        
        if not saving_head_list:
            saving_head = SavingActionHead.objects.create(user=request.user, name=title)
            created = True
        else:
            saving_head = saving_head_list[0]
        saving_head.save()
        
        if not created:
            SavingActionBody.objects.filter(saving_action=saving_head).delete()
        
        number = 1
        continue_battleactions = formset.save(commit=False)
        for continue_battleaction in continue_battleactions:
            saving_body = SavingActionBody.objects.create(saving_action=saving_head, action_no=number)
            saving_body.action_target = continue_battleaction.action_target
            saving_body.action = continue_battleaction.action
            saving_body.perks_id = continue_battleaction.perks_id
            saving_body.save()
            number = number + 1
        
        return False
    
    @classmethod
    def delete(cls, saving_id, request):
        cache.delete(SavingActionBody._get_get_unique_list_cache_key(saving_id))
        cache.delete(SavingActionHead._get_filter_values_cache_key(request.user.id))
        SavingActionBody.objects.filter(saving_action=saving_id).delete()
        SavingActionHead.objects.filter(id=saving_id).delete()
        
        
        
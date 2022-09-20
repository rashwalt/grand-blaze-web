# -*- coding: utf-8 -*-

from django.template.loader import render_to_string
from django.core.cache import cache

from module.character.models import Character
from module.regist.continue_complete.models import ContinueComplete
from module.regist.continue_serif.models import ContinueSerif, SavingSerifHead, SavingSerifBody

class ContinueSerifAPI(object):
    
    @classmethod
    def get(cls, user_id):
        return ContinueSerif.get_filter_by_user(user_id)
    
    @classmethod
    def get_query(cls, user_id):
        return ContinueSerif.objects.filter(user=user_id).order_by('situation_id', 'id')
    
    @classmethod
    def update_continue_serif(cls, request, continue_serifs):
        user = request.user
        
        # 送信者情報
        ip_address = request.META.get('REMOTE_ADDR','')
        host = request.META.get('REMOTE_HOST', '')
        agent = request.META.get('HTTP_USER_AGENT','')
        
        continue_serif_del_list = ContinueSerif.get_filter_by_user(user.id)
        for del_data in continue_serif_del_list:
            del_data.delete()
        
        # Continue Serif multi save
        number = 1
        for temp_data in continue_serifs:
            ContinueSerif.objects.create(user=user, word_no=number, situation_id=temp_data.situation_id, serif_text=temp_data.serif_text, perks_id=temp_data.perks_id, ip_address=ip_address, host_address=host, user_agent=agent)
            number = number + 1
        
        # Continue Complete
        ContinueComplete.completed(user, 'serif', ip_address, host, agent)
    
    @classmethod
    def get_mail(cls, user):
        character = Character.get(user.id)
        
        continue_serifs = cls.get(user.id)
        
        ctxt = {
                'user_id': user.id,
                'character_name': character.character_name,
                'datas': continue_serifs,
                'user': user,
                }
        
        return render_to_string('regist/continue_serif/mail.html', ctxt)
        
class SavingSerifAPI(object):
    
    @classmethod
    def get_head_list(cls, user):
        return SavingSerifHead.get_filter_by_user_values(user)
    
    @classmethod
    def get_head(cls, saving_id):
        return SavingSerifHead.get_values(saving_id)
    
    @classmethod
    def get_body(cls, saving_id):
        return SavingSerifBody.get_unique_list(saving_id)
    
    @classmethod
    def update_saved_action(cls, request, formset, cleaned_data):
        title = cleaned_data['title']
        saving_id = cleaned_data['saving_id']
        
        head_list_count = SavingSerifHead.objects.filter(user=request.user).exclude(name=title).count()
        
        if head_list_count >= 10:
            return True
        
        saving_head, created = SavingSerifHead.objects.get_or_create(user=request.user, name=title)
        saving_head.save()
        
        if not created:
            SavingSerifBody.objects.filter(saving_action=saving_head).delete()
        
        number = 1
        continue_serifs = formset.save(commit=False)
        for continue_serif in continue_serifs:
            saving_body = SavingSerifBody.objects.create(saving_action=saving_head, word_no=number, situation_id=continue_serif.situation_id)
            saving_body.situation_id = continue_serif.situation_id
            saving_body.serif_text = continue_serif.serif_text
            saving_body.perks_id = continue_serif.perks_id
            saving_body.save()
            number = number + 1
        
        return False
    
    @classmethod
    def delete(cls, saving_id, request):
        cache.delete(SavingSerifBody._get_get_unique_list_cache_key(saving_id))
        cache.delete(SavingSerifHead._get_filter_values_cache_key(request.user.id))
        SavingSerifBody.objects.filter(saving_action=saving_id).delete()
        SavingSerifHead.objects.filter(id=saving_id).delete()
        
        
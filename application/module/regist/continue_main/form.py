# -*- coding: utf-8 -*-

from django import forms

from module.regist.continue_main.models import ContinueMain

from module.regist.constant import RegistConstant
from django.contrib.auth.models import User

class ContinueMainForm(forms.ModelForm):
    party_secession = forms.ChoiceField(widget=forms.RadioSelect(), choices=RegistConstant.PARTY_SECESSIONS, initial=RegistConstant.PARTY_SECESSION_STAY)
    party_hope = forms.ChoiceField(widget=forms.RadioSelect(), choices=RegistConstant.PARTY_HOPES, initial=RegistConstant.PARTY_HOPE_STAY)
    quest_id = forms.ChoiceField(initial=0)
    mark_id = forms.ChoiceField(initial=0)
        
    class Meta:
        model = ContinueMain
        exclude = ('user', 'ip_address', 'host_address', 'user_agent', 'created_at', 'updated_at')
        
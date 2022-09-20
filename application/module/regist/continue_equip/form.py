# -*- coding: utf-8 -*-

from django import forms

from module.regist.continue_equip.models import ContinueEquip

from module.regist.constant import RegistConstant
from django.contrib.auth.models import User

class ContinueEquipForm(forms.ModelForm):
    install = forms.ChoiceField(initial=0, required=False)
    secondary_install = forms.ChoiceField(initial=0, required=False)
        
    class Meta:
        model = ContinueEquip
        exclude = ('user', 'ip_address', 'host_address', 'user_agent', 'created_at', 'updated_at')
        
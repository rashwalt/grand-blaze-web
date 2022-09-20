# -*- coding: utf-8 -*-

from django import forms

from module.regist.continue_profile.models import ContinueProfile

from module.regist.constant import RegistConstant
from django.contrib.auth.models import User

class ContinueProfileForm(forms.ModelForm):
    account_status = forms.ChoiceField(choices=RegistConstant.ACCOUNT_STATUS, initial=RegistConstant.ACCOUNT_STAT_ACTIVE)
    image_url = forms.URLField(label=u'イメージURL', required=False)
    image_link_url = forms.URLField(label=u'イメージリンクURL', required=False)
        
    class Meta:
        model = ContinueProfile
        exclude = ('user', 'ip_address', 'host_address', 'user_agent', 'created_at', 'updated_at')
        
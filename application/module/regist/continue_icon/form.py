# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import modelformset_factory

from module.regist.continue_icon.models import ContinueIcon

from module.regist.constant import RegistConstant
from django.contrib.auth.models import User

class ContinueIconForm(forms.ModelForm):
    icon_url = forms.URLField(label=u'アイコンURL', required=True)
        
    class Meta:
        model = ContinueIcon
        exclude = ('user', 'ip_address', 'host_address', 'user_agent', 'created_at', 'updated_at')

ContinueIconFormSet = modelformset_factory(ContinueIcon, form=ContinueIconForm, max_num=50, extra=0, can_delete=True)

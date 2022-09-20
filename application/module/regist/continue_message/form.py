# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import modelformset_factory

from module.regist.continue_message.models import ContinueMessage

from module.regist.constant import RegistConstant
from django.contrib.auth.models import User

class ContinueMessageForm(forms.ModelForm):
        
    class Meta:
        model = ContinueMessage
        exclude = ('user', 'ip_address', 'host_address', 'user_agent', 'created_at', 'updated_at')

ContinueMessageFormSet = modelformset_factory(ContinueMessage, form=ContinueMessageForm, extra=0, can_delete=True)
ContinueMessageFormSetInitial = modelformset_factory(ContinueMessage, form=ContinueMessageForm, extra=1, can_delete=True)

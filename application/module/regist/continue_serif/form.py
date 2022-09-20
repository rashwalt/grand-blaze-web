# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import modelformset_factory

from module.regist.continue_serif.models import ContinueSerif

from module.regist.constant import RegistConstant
from django.contrib.auth.models import User

class ContinueSerifForm(forms.ModelForm):
        
    class Meta:
        model = ContinueSerif
        exclude = ('user', 'ip_address', 'host_address', 'user_agent', 'created_at', 'updated_at')

ContinueSerifFormSet = modelformset_factory(ContinueSerif, form=ContinueSerifForm, extra=0, can_delete=True)

class SavingSerifForm(forms.Form):
    saving_id = forms.ChoiceField(label=u'保存済みセリフ', initial=0, required=False)
    title = forms.CharField(label=u'セリフセット名', max_length=100, required=False)
    
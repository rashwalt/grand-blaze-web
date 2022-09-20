# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import modelformset_factory

from module.regist.continue_battleaction.models import ContinueBattleAction

from module.regist.constant import RegistConstant
from django.contrib.auth.models import User

class ContinueBattleActionForm(forms.ModelForm):
    action = forms.ChoiceField(initial=0)
    
    def clean_perks_id(self):
        _action = self.cleaned_data['action'] if 'action' in self.cleaned_data else None
        _perks_id = self.cleaned_data['perks_id'] if 'perks_id' in self.cleaned_data else None
        if _action and int(_action) == 1 and _perks_id:
            raise forms.ValidationError(u'アーツ指定が記入されていますが、アクションが「物理攻撃」になっています。')
        elif not _action or (int(_action) == 2 or int(_action) == 3) and not _perks_id:
            raise forms.ValidationError(u'発動するアーツ・スペシャルが指定されていません。')
        else:
            return _perks_id
        
    class Meta:
        model = ContinueBattleAction
        exclude = ('user', 'ip_address', 'host_address', 'user_agent', 'created_at', 'updated_at')

ContinueBattleActionFormSet = modelformset_factory(ContinueBattleAction, form=ContinueBattleActionForm, max_num=10, extra=0, can_delete=True)

class SavingActionForm(forms.Form):
    saving_id = forms.ChoiceField(label=u'保存済みアクション', initial=0, required=False)
    title = forms.CharField(label=u'戦術名', max_length=100, required=False)
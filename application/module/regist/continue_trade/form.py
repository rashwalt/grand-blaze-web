# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import modelformset_factory

from module.regist.continue_trade.models import ContinueShopping, ContinueTrade

from module.regist.constant import RegistConstant
from django.contrib.auth.models import User

class ContinueShoppingForm(forms.ModelForm):
        
    class Meta:
        model = ContinueShopping
        exclude = ('user', 'ip_address', 'host_address', 'user_agent', 'created_at', 'updated_at')

ContinueShoppingFormSet = modelformset_factory(ContinueShopping, form=ContinueShoppingForm, max_num=5, extra=5)
ContinueShoppingFormSetInitial = modelformset_factory(ContinueShopping, form=ContinueShoppingForm, max_num=5, extra=5)

class ContinueTradeForm(forms.ModelForm):
        
    class Meta:
        model = ContinueShopping
        exclude = ('user', 'ip_address', 'host_address', 'user_agent', 'created_at', 'updated_at')

ContinueTradeFormSet = modelformset_factory(ContinueTrade, form=ContinueTradeForm, max_num=5, extra=5)
ContinueTradeFormSetInitial = modelformset_factory(ContinueTrade, form=ContinueTradeForm, max_num=5, extra=5)
    
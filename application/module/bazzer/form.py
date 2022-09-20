# -*- coding:utf-8 -*-

from django import forms

from module.bazzer.models import Bazzer
from module.bazzer.constant import BazzerConstant

class BazzerSearchForm(forms.Form):
    type = forms.ChoiceField(label=u'種別', initial=0)
    level = forms.IntegerField(label=u'装備レベル', required=False)
    min_price = forms.IntegerField(label=u'金額（最小）', required=False)
    max_price = forms.IntegerField(label=u'金額（最大）', required=False)
    sort = forms.ChoiceField(label=u'ソート', choices=BazzerConstant.SORT_LIST)
    is_mine = forms.BooleanField(label=u'自分の出品だけ表示', required=False, initial=False)
    is_buy = forms.BooleanField(label=u'自分の落札物だけ表示', required=False, initial=False)

class BazzerSellForm(forms.ModelForm):
        
    class Meta:
        model = Bazzer
        exclude = ('seller', 'item', 'buyer', 'seller_date', 'status', 'created_at', 'updated_at')
    
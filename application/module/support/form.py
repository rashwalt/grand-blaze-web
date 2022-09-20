# -*- coding: utf-8 -*-

from django import forms

from module.support.constant import SupportConstant

class SupportForm(forms.Form):
    name = forms.CharField(label=u'名前')
    entry_no = forms.DecimalField(label=u'エントリーナンバー', required=False, decimal_places=0)
    from_mail = forms.EmailField(label=u'メール')
    subject = forms.ChoiceField(label=u'お問い合わせ内容', choices=SupportConstant.SUBJECTS)
    body = forms.CharField(label=u'本文', widget=forms.Textarea)
# -*- coding: utf-8 -*-

from django import forms

from library.zenhan import z2h

from module.regist.newgame.models import NewGame

from module.regist.constant import RegistConstant
from django.contrib.auth.models import User

class NewGameForm(forms.ModelForm):
    sex = forms.ChoiceField(widget=forms.RadioSelect(), choices=RegistConstant.SEXS, initial=RegistConstant.SEX_UNKNOWN)
    install_class_id = forms.ChoiceField(initial=1)
    race_id = forms.ChoiceField(initial=1)
    
    name = forms.CharField(label=u'名前')
    email = forms.EmailField(label=u'メールアドレス')
    password = forms.CharField(label=u'パスワード', widget=forms.PasswordInput)
    password_conf = forms.CharField(label=u'パスワード（確認）', widget=forms.PasswordInput)
    
    image_url = forms.URLField(label=u'イメージURL', required=False)
    image_link_url = forms.URLField(label=u'イメージリンクURL', required=False)
    
    def clean_password_conf(self):
        _password = self.cleaned_data['password'] if 'password' in self.cleaned_data else None
        _password_conf = self.cleaned_data['password_conf'] if 'password_conf' in self.cleaned_data else None
        if not _password or not _password_conf and _password != _password_conf:
            raise forms.ValidationError(u'パスワード（確認）が異なります。')
        else:
            return _password_conf
        
    def clean_email(self):
        _mod_email = self.cleaned_data['email']
        _mod_email = z2h(_mod_email)
        if User.objects.filter(email=_mod_email).exists():
            raise forms.ValidationError(u'このメールアドレスでは登録できません。')
        return _mod_email
        
    class Meta:
        model = NewGame
        exclude = ('user', 'ip_address', 'host_address', 'user_agent', 'created_at', 'updated_at', 'activate')
        
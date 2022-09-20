# -*- coding: utf-8 -*-

from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import User

class AccountLoginForm(forms.Form):
    email = forms.EmailField(label=u'メールアドレス')
    password = forms.CharField(label=u'パスワード', widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label=u'ログイン状態を保持する', required=False, initial=True)

class AccountSettingForm(forms.Form):
    user_id = forms.CharField(label=u'ユーザID', widget=forms.HiddenInput)
    name = forms.CharField(label=u'名前')
    mod_email = forms.EmailField(label=u'メールアドレス')
    official_news = forms.BooleanField(label=u'公式からのお知らせ配信を受け取る', required=False, initial=True)
    continue_mail = forms.BooleanField(label=u'各種登録内容の自動配信を受け取る', required=False, initial=True)
    message_mail = forms.BooleanField(label=u'未読メッセージの配信を受け取る', required=False, initial=True)
    
    def clean_mod_email(self):
        _mod_email = self.cleaned_data['mod_email']
        _user_id = self.cleaned_data['user_id']
        if User.objects.filter(email=_mod_email).exclude(id=_user_id).exists():
            raise forms.ValidationError(u'このメールアドレスでは登録できません。')
        return _mod_email
        
    
class AccountPasswordChangeForm(forms.Form):
    mod_password = forms.CharField(label=u'パスワード', widget=forms.PasswordInput)
    mod_password_conf = forms.CharField(label=u'パスワード（確認）', widget=forms.PasswordInput)
    
    def clean_mod_password_conf(self):
        _mod_password = self.cleaned_data['mod_password']
        _mod_password_conf = self.cleaned_data['mod_password_conf']
        if _mod_password != _mod_password_conf:
            raise forms.ValidationError(u'パスワード（確認）が異なります。')
        else:
            return _mod_password_conf

class MessageForm(forms.Form):
    entry_no = forms.DecimalField(label=u'送信先', decimal_places=0)
    entry_no2 = forms.DecimalField(label=u'送信先2', decimal_places=0, required=False)
    entry_no3 = forms.DecimalField(label=u'送信先3', decimal_places=0, required=False)
    entry_no4 = forms.DecimalField(label=u'送信先4', decimal_places=0, required=False)
    entry_no5 = forms.DecimalField(label=u'送信先5', decimal_places=0, required=False)
    title = forms.CharField(label=u'件名', max_length=140)
    body = forms.CharField(label=u'本文', widget=forms.Textarea)
    
    def clean_entry_no(self):
        _mod_entry = self.cleaned_data['entry_no']
        if int(_mod_entry) < 10:
            raise forms.ValidationError(u'送信可能な相手が見つかりません。')
        elif not User.objects.filter(id=int(_mod_entry)).exists():
            raise forms.ValidationError(u'送信可能な相手が見つかりません。')
        else:
            return _mod_entry
        
    def clean_entry_no2(self):
        _mod_entry = self.cleaned_data['entry_no2']
        if _mod_entry:
            if int(_mod_entry) < 10:
                raise forms.ValidationError(u'送信可能な相手が見つかりません。')
            elif not User.objects.filter(id=int(_mod_entry)).exists():
                raise forms.ValidationError(u'送信可能な相手が見つかりません。')
        
        return _mod_entry
        
    def clean_entry_no3(self):
        _mod_entry = self.cleaned_data['entry_no3']
        if _mod_entry:
            if int(_mod_entry) < 10:
                raise forms.ValidationError(u'送信可能な相手が見つかりません。')
            elif not User.objects.filter(id=int(_mod_entry)).exists():
                raise forms.ValidationError(u'送信可能な相手が見つかりません。')
        
        return _mod_entry
        
    def clean_entry_no4(self):
        _mod_entry = self.cleaned_data['entry_no4']
        if _mod_entry:
            if int(_mod_entry) < 10:
                raise forms.ValidationError(u'送信可能な相手が見つかりません。')
            elif not User.objects.filter(id=int(_mod_entry)).exists():
                raise forms.ValidationError(u'送信可能な相手が見つかりません。')
        
        return _mod_entry
        
    def clean_entry_no5(self):
        _mod_entry = self.cleaned_data['entry_no5']
        if _mod_entry:
            if int(_mod_entry) < 10:
                raise forms.ValidationError(u'送信可能な相手が見つかりません。')
            elif not User.objects.filter(id=int(_mod_entry)).exists():
                raise forms.ValidationError(u'送信可能な相手が見つかりません。')
        
        return _mod_entry
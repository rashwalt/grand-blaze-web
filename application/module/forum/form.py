# -*- coding: utf-8 -*-

from django import forms
from captcha.fields import CaptchaField

from module.forum.constant import ForumConstant

class ThreadForm(forms.Form):
    title = forms.CharField(label=u'スレッド名', max_length=140)
    body = forms.CharField(label=u'本文', widget=forms.Textarea)
    forum_status = forms.ChoiceField(label=u'フォーラムステータス')
    is_rock = forms.BooleanField(label=u'スレッドのロック', required=False, initial=False)
    thread_solid = forms.BooleanField(label=u'位置固定スレッド', required=False, initial=False)
    preview = forms.BooleanField(label=u'プレビュー', required=False, initial=False)

class NotAuthThreadForm(forms.Form):
    title = forms.CharField(label=u'スレッド名', max_length=140)
    create_user_name = forms.CharField(label=u'作成者', max_length=140)
    body = forms.CharField(label=u'本文', widget=forms.Textarea)
    forum_status = forms.ChoiceField(label=u'フォーラムステータス')
    status_change_pass = forms.CharField(label=u'変更パス', max_length=16)
    preview = forms.BooleanField(label=u'プレビュー', required=False, initial=False)
    captcha = CaptchaField()

class ArticleForm(forms.Form):
    body = forms.CharField(label=u'本文', widget=forms.Textarea)
    user_name = forms.CharField(label=u'投稿者', max_length=140, required=False, initial='')
    forum_status = forms.ChoiceField(label=u'フォーラムステータス', required=False)
    is_rock = forms.BooleanField(label=u'スレッドのロック', required=False, initial=False)
    preview = forms.BooleanField(label=u'この返信をプレビュー', required=False, initial=False)

class NotAuthArticleForm(forms.Form):
    body = forms.CharField(label=u'本文', widget=forms.Textarea)
    user_name = forms.CharField(label=u'投稿者', max_length=140, required=False, initial='')
    forum_status = forms.ChoiceField(label=u'フォーラムステータス', required=False)
    status_change_pass = forms.CharField(label=u'変更パス', max_length=16, required=False)
    preview = forms.BooleanField(label=u'この返信をプレビュー', required=False, initial=False)
    captcha = CaptchaField()

class ArticleEditForm(forms.Form):
    body = forms.CharField(label=u'本文', widget=forms.Textarea)
    edit_mean = forms.CharField(label=u'編集理由', widget=forms.Textarea)
    preview = forms.BooleanField(label=u'この返信をプレビュー', required=False, initial=False)

class ArticleDeleteForm(forms.Form):
    delete_mean = forms.CharField(label=u'削除理由', widget=forms.Textarea)

class ThreadSearchForm(forms.Form):
    body = forms.CharField(label=u'検索本文')
    choice_type = forms.ChoiceField(label=u'条件指定', widget=forms.RadioSelect, choices=ForumConstant.CHOICE_TYPES, initial=ForumConstant.CHOICE_TYPE_AND)
    forum_id = forms.ChoiceField(label=u'検索対象', initial=0)
    
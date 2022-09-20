# -*- coding: utf-8 -*-

from django import forms

class CharacterSearchForm(forms.Form):
    body = forms.CharField(label=u'検索本文')
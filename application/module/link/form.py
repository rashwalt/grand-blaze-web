# -*- coding: utf-8 -*-

from django import forms

from module.link.models import Link

from django.contrib.auth.models import User

class LinkForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)
    url = forms.URLField()
        
    class Meta:
        model = Link
        exclude = ('user', 'created_at', 'updated_at')
        
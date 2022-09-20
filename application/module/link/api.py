# -*- coding: utf-8 -*-

from django.contrib import messages
from django.conf import settings

from library.send_mail import send_mail

from module.link.models import Link, LinkCategory

class LinkAPI(object):
    
    @classmethod
    def get_category_top(cls, category):
        
        return Link.get_category_top(category)
    
    @classmethod
    def get(cls, user_id):
        return Link.get(user_id)
    
    @classmethod
    def update_link(cls, request, model_form):
        user = request.user
        email = user.email
        
        # Link save
        link = model_form.save(commit=False)
        link.user = user
        link.save()
        
        subject = u"[Grand Blaze] : リンク申請があります！"  
        
        mail_body = u"""
本メールはリンク申請からの送信です。

申請者：
%s (E-No. %s)

申請サイト：
URL: %s
%s

%s
""" % (link.owner, user.id, link.url, link.name, link.comment)
        
        # 送信
        send_mail(subject, mail_body, email, [settings.MAIL_FROM])
        
        messages.success(request, u'サイト情報を申請・変更しました。')

class LinkCategoryAPI(object):
    
    @classmethod
    def get_category_list(cls):
        return LinkCategory.get_category_list()
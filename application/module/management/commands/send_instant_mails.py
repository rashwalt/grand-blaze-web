# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.management.base import BaseCommand

from library.send_mail import send_mail

from module.account.models import InstantMessage

from module.account.api import UserProfileAPI

class Command(BaseCommand):
    
    def handle(self, *args, **option):
        notreads = InstantMessage.get_last()
        
        for message in notreads:
            notread_count = InstantMessage.get_read_complete_count(message['user'])
            
            if not notread_count:
                continue
            
            user = UserProfileAPI.get_user(message['user'])
            profile = UserProfileAPI.get_or_create_user_profile_by_user(user)
            
            if not profile.message_mail:
                continue
            
            subject = u"[Grand Blaze] : %s件の未読メッセージがあります!" % notread_count
            
            body = u"""
%s 様

Grand Blazeのインスタントメッセージに%s件の未読メッセージが届いています!

最新の未読メッセージをサイトにログインした後、ご確認下さい!

メッセージの確認はこちら!
http://www.grand-blaze.com/message/

--------------------------------------------------------------

本メールはGrand Blaze各種登録からの自動送信です。
身に覚えのない場合は、お手数ですが削除をお願いいたします。

-------------------------------------------------------------
Grand Blaze
http://www.grand-blaze.com/
-------------------------------------------------------------
""" % (user.email, notread_count)
            send_mail(subject, body, settings.MAIL_FROM, [user.email])
            
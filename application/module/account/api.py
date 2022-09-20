# -*- coding: utf-8 -*-

from django.contrib import messages
from django.conf import settings
from django.utils.http import int_to_base36, base36_to_int
from django.contrib.auth.tokens import default_token_generator

from django.contrib.auth.models import User

from module.account.models import UserProfile, InstantMessage

from library.send_mail import send_mail

class UserProfileAPI(object):
    
    @classmethod
    def get_or_create_user_profile_by_user(cls, user):
        if not user.is_authenticated():
            return None
        profile = None
        try:
            profile = user.get_profile()
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=user)
        return profile
    
    @classmethod
    def get_or_create_user_profile(cls, request):
        profile = None
        user = request.user
        if not user.is_authenticated():
            return None
        try:
            profile = user.get_profile()
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=user)
        return profile
    
    @classmethod
    def get_user_profile(cls, request):
        profile = None
        user = request.user
        if not user.is_authenticated():
            return None
        try:
            profile = user.get_profile()
        except UserProfile.DoesNotExist:
            pass
        return profile
    
    @classmethod
    def update_user_profile(cls, request, cleaned_data):
        name = cleaned_data['name']
        mod_email = cleaned_data['mod_email']
        official_news = cleaned_data['official_news']
        continue_mail = cleaned_data['continue_mail']
        message_mail = cleaned_data['message_mail']
        
        user_profile = cls.get_or_create_user_profile(request)
        user_profile.user_name = name
        user_profile.official_news = official_news
        user_profile.continue_mail = continue_mail
        user_profile.message_mail = message_mail
        user_profile.save()
        
        user = request.user
        user.email = mod_email
        user.save()
        
        messages.success(request, u'アカウント情報を変更しました。')
    
    @classmethod
    def update_password(cls, request, cleaned_data):
        mod_password = cleaned_data['mod_password']
        
        user = request.user
        user.set_password(mod_password)
        user.save()
        
        messages.success(request, u'パスワードを変更しました。')
    
    @classmethod
    def update_password_by_user(cls, request, user, cleaned_data):
        mod_password = cleaned_data['mod_password']
        
        user.set_password(mod_password)
        user.save()
        
        messages.success(request, u'パスワードを変更しました。')
        
    @classmethod
    def get_user_name(cls, user):
        profile = None
        try:
            profile = user.get_profile()
        except UserProfile.DoesNotExist:
            pass
        
        if profile:
            if not user.is_staff:
                return u'%s (%s)' % (profile.user_name, user.id)
            else:
                return profile.user_name
        return ''
        
    @classmethod
    def get_user_name_only(cls, user):
        profile = None
        try:
            profile = user.get_profile()
        except UserProfile.DoesNotExist:
            pass
        
        if profile:
            return profile.user_name
        return ''
    
    @classmethod
    def check_and_get_active_records(cls, activate_hash):
        return UserProfile.check_and_get_active_records(activate_hash)
    
    @classmethod
    def update_reset_password(cls, request, cleaned_data, users_cache):
        email = cleaned_data['email']
        
        for user in users_cache:
            
            uid = int_to_base36(user.id)
            token = default_token_generator.make_token(user)
            
            subject = u"[Grand Blaze] : パスワードリセットのお知らせ"        
            
            mail_body = u"""
%s 様

Grand Blazeに登録されているアカウントについて、パスワードリセットが要求されました。

以下のアドレスにアクセスして頂き、パスワードの変更を行ってください。

http://www.grand-blaze.com/account/prs/%s-%s/

本メールはGrand Blazeパスワードリセットからの自動送信です。
身に覚えのない場合は、お手数ですが削除をお願いいたします。

-------------------------------------------------------------
Grand Blaze
http://www.grand-blaze.com/
-------------------------------------------------------------
""" % (email, uid, token)
            
            # 送信
            send_mail(subject, mail_body, settings.MAIL_FROM, [email])
    
            messages.success(request, u'パスワードリセットのメールを送信しました。')
            return
        
    @classmethod
    def get_user_from_uidb36(cls, uidb36):
        try:
            uid_int = base36_to_int(uidb36)
            user = User.objects.get(id=uid_int)
        except (ValueError, User.DoesNotExist):
            user = None
        
        return user
    
    @classmethod
    def get_user(cls, user_id):
        try:
            user = User.objects.get(id=user_id)
        except (ValueError, User.DoesNotExist):
            user = None
        
        return user
        


class InstantMessageAPI(object):
    
    @classmethod
    def get_to_user_list(cls, user):
        return InstantMessage.get_to_user_list(user)
    
    @classmethod
    def get_from_user_list(cls, user):
        return InstantMessage.get_from_user_list(user)

    @classmethod
    def get(cls, key_id):
        return InstantMessage.get(key_id)

    @classmethod
    def update_read_complete(cls, message):
        if not message.read_complete:
            message.read_complete = True
            message.save()
    
    @classmethod
    def update_message(cls, request, cleaned_data):
        entry_no = cleaned_data['entry_no']
        title = cleaned_data['title']
        body = cleaned_data['body']
        entry_no2 = cleaned_data['entry_no2']
        entry_no3 = cleaned_data['entry_no3']
        entry_no4 = cleaned_data['entry_no4']
        entry_no5 = cleaned_data['entry_no5']
        
        message = InstantMessage.objects.create(user_id=entry_no, from_user=request.user, title=title, body=body)
        message.save()
        
        if entry_no2:
            message2 = InstantMessage.objects.create(user_id=entry_no2, from_user=request.user, title=title, body=body)
            message2.save()
        
        if entry_no3:
            message3 = InstantMessage.objects.create(user_id=entry_no3, from_user=request.user, title=title, body=body)
            message3.save()
        
        if entry_no4:
            message4 = InstantMessage.objects.create(user_id=entry_no4, from_user=request.user, title=title, body=body)
            message4.save()
        
        if entry_no5:
            message5 = InstantMessage.objects.create(user_id=entry_no5, from_user=request.user, title=title, body=body)
            message5.save()
        
        messages.success(request, u'メッセージを送信しました。')
    
    @classmethod
    def get_read_complete_count(cls, user):
        return InstantMessage.get_read_complete_count(user)

    
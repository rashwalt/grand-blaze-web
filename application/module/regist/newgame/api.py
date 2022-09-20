# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.hashcompat import sha_constructor
from django.template.loader import render_to_string

from django.contrib.auth.models import User

from library.send_mail import send_mail

from module.regist.newgame.models import NewGame
from module.character.models import Character
from module.account.api import UserProfileAPI
from django.db.utils import IntegrityError

class NewGameAPI(object):
    
    @classmethod
    def get(cls, user_id):
        return NewGame.get(user_id)
    
    @classmethod
    def create_user_and_newgame(cls, request, model_form):
        name = model_form.cleaned_data['name']
        email = model_form.cleaned_data['email']
        password = model_form.cleaned_data['password']
        
        dummy_username = email[:30]
        
        # アクティベートハッシュ
        pass_activate = sha_constructor(email).hexdigest()
        
        try:
            user = User.objects.create_user(dummy_username, email, password)
            user.is_active = False
            user.save()
            user.is_anonymous = False
        except IntegrityError:
            return False
        
        user_profile = UserProfileAPI.get_or_create_user_profile_by_user(user)
        user_profile.user_name = name
        user_profile.official_news = True
        user_profile.continue_mail = True
        user_profile.message_mail = True
        user_profile.pass_activate = pass_activate
        user_profile.save()
        
        # 送信者情報
        ip_address = request.META.get('REMOTE_ADDR','')
        host = request.META.get('REMOTE_HOST', '')
        agent = request.META.get('HTTP_USER_AGENT','')
        
        # NewGame save
        newgame = model_form.save(commit=False)
        newgame.user = user
        newgame.ip_address = ip_address
        newgame.host_address = host
        newgame.user_agent = agent
        newgame.save()
        
        subject = u"[Grand Blaze] : 新規登録 仮登録のお知らせ"        
        
        mail_body = u"""
%s 様

Grand Blazeにご登録頂き、誠にありがとうございます。
新規登録の仮受け付けが完了しました。

24時間以内に、以下のアドレスにアクセスして頂き、本登録を完了してください。

http://www.grand-blaze.com/new_game/compr/%s

本メールはGrand Blaze新規登録からの自動送信です。
身に覚えのない場合は、お手数ですが削除をお願いいたします。

-------------------------------------------------------------
Grand Blaze
http://www.grand-blaze.com/
-------------------------------------------------------------
""" % (email, pass_activate)
        
        # 送信
        send_mail(subject, mail_body, settings.MAIL_FROM, [email])
        return True
    
    @classmethod
    def compare_newgame(cls, request, user):
        
        # NewGame save
        newgame = NewGame.get(user.id)
        
        if newgame.activate == 1:
            return
        
        newgame.activate = 1
        newgame.save()
        
        # Character Create
        character = Character.objects.create(user=user)
        character.character_name = newgame.character_name
        character.image_url = newgame.image_url
        character.image_width = newgame.image_width
        character.image_height = newgame.image_height
        character.image_link_url = newgame.image_link_url
        character.image_copyright = newgame.image_copyright
        character.nick_name = newgame.nick_name
        character.race_id = newgame.race_id
        character.guardian_id = newgame.guardian_id
        character.nation_id = newgame.nation_id
        character.age = newgame.age
        character.sex = newgame.sex
        character.unique_name = newgame.unique_name
        character.height = newgame.height
        character.weight = newgame.weight
        character.save()
        
        user.is_active = True
        user.save()
        
        email = user.email
        
        subject = u"[Grand Blaze] : 新規登録 完了のお知らせ"        
        
        mail_body = u"""
%s 様

Grand Blazeにご登録頂き、誠にありがとうございます。
新規登録の受け付けが完了しました。

早速、ログインを行いましょう！
ログインするには、Grand Blaze公式サイトの右上にある「ログイン」をクリックし、表示されたログイン画面で「ログインメールアドレス」、「ログインパスワード」を入力してログインします。
無事にログインできたら、継続登録を行い、早速次回の行動を決定しましょう！
次回の冒険結果発表にて、ご自身のキャラクターが登録されていれば、新規登録に関するすべての登録が完了します。

発行されたエントリーナンバー、及び情報は以下の通りです。

_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
ログインメールアドレス：
%s

ログインパスワード：
**** ※登録時に設定したパスワードです。

エントリーナンバー：
%s

キャラクター名：
%s
_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/

エントリーナンバー、ログインメールアドレス、および設定したログインパスワードは大切なものです。
なくさないように十分ご注意下さい。

本メールはGrand Blaze新規登録からの自動送信です。
身に覚えのない場合は、お手数ですが削除をお願いいたします。

-------------------------------------------------------------
Grand Blaze
http://www.grand-blaze.com/
-------------------------------------------------------------
""" % (email, email, user.id, newgame.character_name)
        
        # 送信
        send_mail(subject, mail_body, settings.MAIL_FROM, [email])
    
    @classmethod
    def get_mail(cls, user):
        character = Character.get(user.id)
        
        newgame = cls.get(user.id)
        
        if not newgame:
            return ''
        
        ctxt = {
                'user_id': user.id,
                'character_name': character.character_name,
                'data': newgame,
                'user': user,
                }
        
        return render_to_string('regist/newgame/mail.html', ctxt)
    
        
        
        
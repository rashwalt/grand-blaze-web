# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator

from library.simple_error import SimpleError
from library.pager import get_pager_from_list
from library.text_utils import TextUtil

from module.account.form import AccountLoginForm, AccountSettingForm, AccountPasswordChangeForm, MessageForm
from module.account.api import UserProfileAPI, InstantMessageAPI

def account_login(request):
    """
    ログイン画面
    """
    
    error_message = None
    
    redirect_to = request.REQUEST.get('next', '')
    
    if request.method == 'POST':
        form = AccountLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password =  form.cleaned_data['password']
            remember_me =  form.cleaned_data['remember_me']
            
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    if not remember_me:
                        request.session.set_expiry(0)
                    login(request, user)
                    if redirect_to:
                        return HttpResponseRedirect(redirect_to)
                    else:
                        return HttpResponseRedirect(reverse('root_index'))
                else:
                    return SimpleError(request, u'本登録を完了してください')
            else:
                error_message = u'ログインできませんでした。メールアドレスとパスワードを確認してください。'
    else:
        form = AccountLoginForm()
    
    ctxt = RequestContext(request,{
            'form': form,
            'message': error_message,
            'redirect_to': redirect_to,
                                   })
    return render_to_response('account/login.html', ctxt)

def account_logout(request):
    """
    ログアウト
    """
    logout(request)
    return HttpResponseRedirect(reverse('root_index'))

@login_required
def account_setting(request):
    """
    設定
    """
    
    if request.method == 'POST':
        mode = request.POST.get('mode', 'normal')
        if mode == 'normal':
            posted_data = request.POST.copy()
            posted_data['user_id'] = request.user.id
            form = AccountSettingForm(posted_data)
            if form.is_valid():
                UserProfileAPI.update_user_profile(request, form.cleaned_data)
        elif mode == 'pass':
            pass_form = AccountPasswordChangeForm(request.POST)
            if pass_form.is_valid():
                UserProfileAPI.update_password(request, pass_form.cleaned_data)
    
    user_profile = UserProfileAPI.get_or_create_user_profile(request)
    form = AccountSettingForm(initial={'name': user_profile.user_name, 'mod_email': request.user.email, 'official_news': user_profile.official_news, 'continue_mail': user_profile.continue_mail, 'message_mail': user_profile.message_mail})
    
    pass_form = AccountPasswordChangeForm()
    
    ctxt = RequestContext(request,{
            'form': form,
            'pass_form': pass_form,
                                   })
    return render_to_response('account/setting.html', ctxt)

def account_password_reset(request):
    """
    パスワードリセット
    """
    
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            UserProfileAPI.update_reset_password(request, form.cleaned_data, form.users_cache)
    else:
        form = PasswordResetForm()
    
    ctxt = RequestContext(request,{
            'form': form,
                                   })
    return render_to_response('account/pass_reset.html', ctxt)

def account_password_reset_changer(request, uidb36, token):
    """
    パスワードリセット実行
    """
    
    user = UserProfileAPI.get_user_from_uidb36(uidb36)

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = AccountPasswordChangeForm(request.POST)
            if form.is_valid():
                UserProfileAPI.update_password_by_user(request, user, form.cleaned_data)
        else:
            form = AccountPasswordChangeForm()
    else:
        return SimpleError(request, u'有効期限が切れているか、または不正なアクセスです。再度、新規登録をやり直してください。')
        
    ctxt = RequestContext(request,{
            'form': form,
            'uidb36': uidb36,
            'token': token,
                                   })
    return render_to_response('account/pass_reset_changer.html', ctxt)

@login_required
def message_list(request, page=1):
    """
    メッセージリスト
    """
    message_list = InstantMessageAPI.get_to_user_list(request.user)
    
    pager, message_list = get_pager_from_list(message_list, limit=10, page=page)
    
    
    ctxt = RequestContext(request,{
            'pager': pager,
            'message_list': message_list,
                                   })
    return render_to_response('account/message_list.html', ctxt)

@login_required
def send_message_list(request, page=1):
    """
    送信済メッセージリスト
    """
    message_list = InstantMessageAPI.get_from_user_list(request.user)
    
    pager, message_list = get_pager_from_list(message_list, limit=10, page=page)
    
    
    ctxt = RequestContext(request,{
            'pager': pager,
            'message_list': message_list,
                                   })
    return render_to_response('account/send_message_list.html', ctxt)
    
@login_required
def message_detail(request, message_id):
    """
    メッセージ詳細
    """
    message_id = int(message_id)
    
    message = InstantMessageAPI.get(message_id)
    is_to = False
    
    if request.user.id != message.from_user_id and request.user.id != message.user_id:
        return SimpleError(request, u'このメッセージは表示できません。')
    
    if request.user.id == message.user_id:
        InstantMessageAPI.update_read_complete(message)
        is_to = True
    
    
    ctxt = RequestContext(request,{
            'message': message,
            'is_to': is_to,
                                   })
    return render_to_response('account/message_detail.html', ctxt)
    
@login_required
def message_create(request, reply_message_id):
    """
    メッセージ作成・返信
    """
    reply_message_id = int(reply_message_id)
    page_title = u'メッセージ作成'
    
    if reply_message_id > 0:
        message = InstantMessageAPI.get(reply_message_id)
        page_title = u'%sへの返信' % (message.get_from_user_name())
    else:
        message = None
    
    if request.method == 'POST':
            
        form = MessageForm(request.POST)
        if form.is_valid():
            InstantMessageAPI.update_message(request, form.cleaned_data)
            return HttpResponseRedirect(reverse('account_message_list'))
    else:
        if reply_message_id > 0:
            form = MessageForm(initial={'entry_no': message.from_user_id, 'title': u'Re: %s' % message.title, 'body': TextUtil.linebreaksreply(message.body)})
        else:
            form = MessageForm()
    
    ctxt = RequestContext(request,{
            'reply_message_id': reply_message_id,
            'message': message,
            'page_title': page_title,
            'form': form,
                                   })
    return render_to_response('account/message_create.html', ctxt)
    
@login_required
def my_result(request):
    """
    自分の結果
    """
    return HttpResponseRedirect(reverse('result_private_status', args=['%04d' % request.user.id]))


    
    
    


# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from library.simple_error import SimpleError

from module.regist.continue_profile.models import ContinueProfile
from module.regist.continue_profile.form import ContinueProfileForm
from module.regist.continue_profile.api import ContinueProfileAPI
from module.character.api import CharacterAPI

from module.master.management.decorators import check_registration
from module.character.decorators import having_character

@login_required
@check_registration
@having_character
def index(request):
    """
    登録ページ インデックス
    """
    user = request.user

    instance = ContinueProfileAPI.get(user.id)
        
    if request.method == 'POST':
        if instance:
            form = ContinueProfileForm(request.POST, instance=instance)
        else:
            form = ContinueProfileForm(request.POST)
        
        if form.is_valid():
#            ContinueProfileAPI.update_continue_profile(request, form)
#            return HttpResponseRedirect(reverse('continue_profile_complete'))
            request.session['data'] = form.save(commit=False)
            return HttpResponseRedirect(reverse('continue_profile_confirm'))
    else:
        if 'data' in request.session and isinstance(request.session['data'], ContinueProfile):
            data = request.session['data']
            form = ContinueProfileForm(instance=data)
        else:
            if instance:
                form = ContinueProfileForm(instance=instance)
            else:
                initial_data = ContinueProfileAPI.get_initial_data(user)
                initial_data['profile'] = initial_data['profile'].replace(u'<br />', u'\n')
                form = ContinueProfileForm(initial=initial_data)
    
    ctxt = RequestContext(request,{
            'form': form,
                                   })
    return render_to_response('regist/continue_profile/index.html', ctxt)

@login_required
@check_registration
@having_character
def confirm(request):
    """
    登録ページ 確認
    """
    if not 'data' in request.session or not isinstance(request.session['data'], ContinueProfile):
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
    
    data = request.session['data']
    character = CharacterAPI.get(request.user)
    
    ctxt = RequestContext(request,{
            'data': data,
            'character': character,
                                   })
    return render_to_response('regist/continue_profile/confirm.html', ctxt)

@login_required
@require_POST
@check_registration
@having_character
def execute(request):
    """
    登録ページ 実行
    """
    if not 'data' in request.session or not isinstance(request.session['data'], ContinueProfile):
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
    
    data = request.session['data']
    
    ContinueProfileAPI.update_continue_profile(request, data)
    del request.session['data']
    return HttpResponseRedirect(reverse('continue_profile_complete'))

@login_required
@check_registration
@having_character
def complete(request):
    """
    登録ページ 完了
    """
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('regist/continue_profile/complete.html', ctxt)



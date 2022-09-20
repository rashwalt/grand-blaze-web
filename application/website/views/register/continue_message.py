# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.forms.models import modelformset_factory, model_to_dict

from library.simple_error import SimpleError

from module.regist.continue_message.models import ContinueMessage
from module.regist.continue_message.form import ContinueMessageForm, ContinueMessageFormSet, ContinueMessageFormSetInitial
from module.regist.continue_message.api import ContinueMessageAPI

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

    instances = ContinueMessageAPI.get_query(user.id)
        
    if request.method == 'POST':
        formset = ContinueMessageFormSet(request.POST, queryset=instances)
        
        if formset.is_valid():
#            ContinueMessageAPI.update_continue_message(request, formset)
#            return HttpResponseRedirect(reverse('continue_message_complete'))
            request.session['datas'] = formset.save(commit=False)
            return HttpResponseRedirect(reverse('continue_message_confirm'))
    else:
        if 'datas' in request.session and isinstance(request.session['datas'], list) and request.session['datas'] and isinstance(request.session['datas'][0], ContinueMessage):
            #instances = ContinueMessageAPI.get_query_none(user.id)
            datas = request.session['datas']
            ContinueMessageFormSetReload = modelformset_factory(ContinueMessage, form=ContinueMessageForm, extra=len(datas), can_delete=True)
            data_dicts = []
            for data in datas:
                data_dicts.append(model_to_dict(data))
            formset = ContinueMessageFormSetReload(queryset=instances.none(), initial=data_dicts)
        else:
            if 'datas' in request.session:
                del request.session['datas']
            message_datas = ContinueMessageAPI.get(user.id)
            if message_datas:
                formset = ContinueMessageFormSet(queryset=instances)
            else:
                formset = ContinueMessageFormSetInitial(queryset=instances)
    
    ctxt = RequestContext(request,{
            'formset': formset,
                                   })
    return render_to_response('regist/continue_message/index.html', ctxt)

@login_required
@check_registration
@having_character
def confirm(request):
    """
    登録ページ 確認
    """
    if not 'datas' in request.session or not isinstance(request.session['datas'], list) or not isinstance(request.session['datas'][0], ContinueMessage):
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
    
    user = request.user
    
    datas = request.session['datas']
    
    ctxt = RequestContext(request,{
            'user': user,
            'datas': datas,
                                   })
    return render_to_response('regist/continue_message/confirm.html', ctxt)

@login_required
@require_POST
@check_registration
@having_character
def execute(request):
    """
    登録ページ 実行
    """
    if not 'datas' in request.session or not isinstance(request.session['datas'], list) or not isinstance(request.session['datas'][0], ContinueMessage):
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
    
    datas = request.session['datas']
    
    ContinueMessageAPI.update_continue_message(request, datas)
    del request.session['datas']
    return HttpResponseRedirect(reverse('continue_message_complete'))

@login_required
@check_registration
@having_character
def complete(request):
    """
    登録ページ 完了
    """
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('regist/continue_message/complete.html', ctxt)



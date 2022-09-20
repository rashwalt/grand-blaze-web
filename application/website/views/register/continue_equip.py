# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from library.simple_error import SimpleError

from module.regist.continue_equip.models import ContinueEquip
from module.regist.continue_equip.form import ContinueEquipForm
from module.regist.continue_equip.api import ContinueEquipAPI

from module.master.install.api import InstallAPI
from module.character.api import CharacterHaveItemAPI, CharacterKeyItemAPI

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

    instance = ContinueEquipAPI.get(user.id)
    
    is_subset = False
    chara_keyitem = CharacterKeyItemAPI.get_keyitem(user, 3)
    if chara_keyitem:
        is_subset = True
    
    install_list = InstallAPI.get_choices_list()
    install_list.insert(0, (0, u'変更しない'))
        
    if request.method == 'POST':
        if instance:
            form = ContinueEquipForm(request.POST, instance=instance)
        else:
            form = ContinueEquipForm(request.POST)
        
        form.fields['install'].choices = install_list
        form.fields['secondary_install'].choices = install_list
        if form.is_valid():
#            ContinueEquipAPI.update_continue_equip(request, form, is_subset)
#            return HttpResponseRedirect(reverse('continue_equip_complete'))
            request.session['data'] = form.save(commit=False)
            return HttpResponseRedirect(reverse('continue_equip_confirm'))
    else:
        if 'data' in request.session and isinstance(request.session['data'], ContinueEquip):
            data = request.session['data']
            form = ContinueEquipForm(instance=data)
        else:
            if instance:
                form = ContinueEquipForm(instance=instance)
            else:
                form = ContinueEquipForm()
        form.fields['install'].choices = install_list
        form.fields['secondary_install'].choices = install_list
    
    having_item_list = CharacterHaveItemAPI.get_filter(user)
    
    ctxt = RequestContext(request,{
            'form': form,
            'is_subset': is_subset,
            'having_item_list': having_item_list,
                                   })
    return render_to_response('regist/continue_equip/index.html', ctxt)

@login_required
@check_registration
@having_character
def confirm(request):
    """
    登録ページ 確認
    """
    user = request.user
    
    if not 'data' in request.session or not isinstance(request.session['data'], ContinueEquip):
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
    
    data = request.session['data']
    data.user = user
    
    is_subset = False
    chara_keyitem = CharacterKeyItemAPI.get_keyitem(user, 3)
    if chara_keyitem:
        is_subset = True
    
    ctxt = RequestContext(request,{
            'data': data,
            'is_subset': is_subset,
                                   })
    return render_to_response('regist/continue_equip/confirm.html', ctxt)

@login_required
@require_POST
@check_registration
@having_character
def execute(request):
    """
    登録ページ 実行
    """
    if not 'data' in request.session or not isinstance(request.session['data'], ContinueEquip):
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
    
    user = request.user
    
    is_subset = False
    chara_keyitem = CharacterKeyItemAPI.get_keyitem(user, 3)
    if chara_keyitem:
        is_subset = True
        
    data = request.session['data']
    
    ContinueEquipAPI.update_continue_equip(request, data, is_subset)
    del request.session['data']
    return HttpResponseRedirect(reverse('continue_equip_complete'))

@login_required
@check_registration
@having_character
def complete(request):
    """
    登録ページ 完了
    """
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('regist/continue_equip/complete.html', ctxt)



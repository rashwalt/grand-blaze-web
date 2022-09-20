# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.forms.models import modelformset_factory, model_to_dict

from library.simple_error import SimpleError

from module.regist.continue_battleaction.models import ContinueBattleAction
from module.regist.continue_battleaction.form import ContinueBattleActionFormSet, SavingActionForm, ContinueBattleActionForm
from module.regist.continue_battleaction.api import ContinueBattleActionAPI, SavingActionAPI

from module.character.api import CharacterHaveSkillAPI, CharacterActionAPI
from module.master.battleaction.api import BattleActionAPI, BattleTargetAPI

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

    instances = ContinueBattleActionAPI.get_query(user.id)
    character_actions = []
        
    if request.method == 'POST':
        mode = request.POST.get('mode', None)
        if mode == 'load':
            saving_id = request.POST.get('saving_id', 0)
            saving_id = int(saving_id)
            character_actions = SavingActionAPI.get_body(saving_id)
            saving_head = SavingActionAPI.get_head(saving_id)
            ContinueBattleActionFormSetLoad = modelformset_factory(ContinueBattleAction, form=ContinueBattleActionForm, max_num=10, extra=len(character_actions), can_delete=True)
            formset = ContinueBattleActionFormSetLoad(queryset=instances.none(), initial=character_actions)
            for form in formset.forms:
                form.fields['action'].choices = BattleActionAPI.get_choices_list()
            if not saving_head:
                return SimpleError(request, u'要求された戦術のロードができませんでした。データが存在しません。')
            saving_form = SavingActionForm(initial={ 'saving_id': saving_head[0][0] })
        elif mode == 'delete':
            saving_id = request.POST.get('saving_id', 0)
            saving_id = int(saving_id)
            SavingActionAPI.delete(saving_id, request)
            
            formset = ContinueBattleActionFormSet(queryset=instances)
            for form in formset.forms:
                form.fields['action'].choices = BattleActionAPI.get_choices_list()
            saving_form = SavingActionForm()
            
        elif mode == 'write':
            post_data = request.POST
            saving_action_list = SavingActionAPI.get_head_list(user)
            
            saving_form = SavingActionForm(post_data)
            saving_form.fields['saving_id'].choices = saving_action_list
            
            formset = ContinueBattleActionFormSet(post_data, queryset=instances)
            for form in formset.forms:
                form.fields['action'].choices = BattleActionAPI.get_choices_list()
                
            if saving_form.is_valid() and formset.is_valid():
                is_over = SavingActionAPI.update_saved_action(request, formset, saving_form.cleaned_data)
                if is_over:
                    return SimpleError(request, u'これ以上の戦術を登録できません。')
                saving_form = SavingActionForm()
        else:
            formset = ContinueBattleActionFormSet(request.POST, queryset=instances)
            
            for form in formset.forms:
                form.fields['action'].choices = BattleActionAPI.get_choices_list()
            if formset.is_valid():
#                ContinueBattleActionAPI.update_continue_battleaction(request, formset)
#                return HttpResponseRedirect(reverse('continue_battleaction_complete'))
                request.session['datas'] = formset.save(commit=False)
                return HttpResponseRedirect(reverse('continue_battleaction_confirm'))
            saving_form = SavingActionForm()
    else:
        if 'datas' in request.session and isinstance(request.session['datas'], list) and request.session['datas'] and isinstance(request.session['datas'][0], ContinueBattleAction):
            datas = request.session['datas']
            ContinueBattleActionFormSetReload = modelformset_factory(ContinueBattleAction, form=ContinueBattleActionForm, extra=len(datas), can_delete=True)
            data_dicts = []
            for data in datas:
                data_dicts.append(model_to_dict(data))
            formset = ContinueBattleActionFormSetReload(queryset=instances.none(), initial=data_dicts)
        else:
            if 'datas' in request.session:
                del request.session['datas']
            basic_list = ContinueBattleActionAPI.get(user.id)
            if basic_list:
                formset = ContinueBattleActionFormSet(queryset=instances)
            else:
                character_actions = CharacterActionAPI.get_chices_list(user)
                ContinueBattleActionFormSetInitial = modelformset_factory(ContinueBattleAction, form=ContinueBattleActionForm, max_num=10, extra=len(character_actions)+1)
                if character_actions:
                    formset = ContinueBattleActionFormSetInitial(queryset=instances, initial=character_actions)
                else:
                    formset = ContinueBattleActionFormSetInitial(queryset=instances)
        for form in formset.forms:
            form.fields['action'].choices = BattleActionAPI.get_choices_list()
        saving_form = SavingActionForm()
        
    saving_form.fields['saving_id'].choices = SavingActionAPI.get_head_list(user)
        
    skill_list = CharacterHaveSkillAPI.get_using(user)
    
    target_list = BattleTargetAPI.get_choices_list()
    
    ctxt = RequestContext(request,{
            'formset': formset,
            'skill_list': skill_list,
            'target_list': target_list,
            'saving_form': saving_form,
            'character_actions': character_actions,
                                   })
    return render_to_response('regist/continue_battleaction/index.html', ctxt)

@login_required
@check_registration
@having_character
def confirm(request):
    """
    登録ページ 確認
    """
    if not 'datas' in request.session or not isinstance(request.session['datas'], list) or not isinstance(request.session['datas'][0], ContinueBattleAction):
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
    
    user = request.user
    
    datas = request.session['datas']
    
    ctxt = RequestContext(request,{
            'user': user,
            'datas': datas,
                                   })
    return render_to_response('regist/continue_battleaction/confirm.html', ctxt)

@login_required
@require_POST
@check_registration
@having_character
def execute(request):
    """
    登録ページ 実行
    """
    if not 'datas' in request.session or not isinstance(request.session['datas'], list) or not isinstance(request.session['datas'][0], ContinueBattleAction):
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
    
    datas = request.session['datas']
    
    ContinueBattleActionAPI.update_continue_battleaction(request, datas)
    del request.session['datas']
    return HttpResponseRedirect(reverse('continue_battleaction_complete'))

@login_required
@check_registration
@having_character
def complete(request):
    """
    登録ページ 完了
    """
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('regist/continue_battleaction/complete.html', ctxt)



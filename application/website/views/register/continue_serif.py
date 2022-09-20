# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.forms.models import modelformset_factory, model_to_dict

from library.simple_error import SimpleError

from module.regist.continue_serif.models import ContinueSerif
from module.master.situation.api import SituationAPI
from module.character.api import CharacterHaveSkillAPI, CharacterSerifAPI

from module.regist.continue_serif.form import ContinueSerifFormSet, ContinueSerifForm, SavingSerifForm
from module.regist.continue_serif.api import ContinueSerifAPI, SavingSerifAPI

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

    instances = ContinueSerifAPI.get_query(user.id)
    character_serifs = []
        
    if request.method == 'POST':
        mode = request.POST.get('mode', None)
        if mode == 'load':
            saving_id = request.POST.get('saving_id', 0)
            saving_id = int(saving_id)
            character_serifs = SavingSerifAPI.get_body(saving_id)
            saving_head = SavingSerifAPI.get_head(saving_id)
            ContinueSerifFormSetLoad = modelformset_factory(ContinueSerif, form=ContinueSerifForm, extra=len(character_serifs), can_delete=True)
            formset = ContinueSerifFormSetLoad(queryset=instances.none(), initial=character_serifs)
            if not saving_head:
                return SimpleError(request, u'要求されたセリフセットのロードができませんでした。データが存在しません。')
            saving_form = SavingSerifForm(initial={ 'saving_id': saving_head[0][0] })
        elif mode == 'delete':
            saving_id = request.POST.get('saving_id', 0)
            saving_id = int(saving_id)
            SavingSerifAPI.delete(saving_id, request)
            
            formset = ContinueSerifFormSet(queryset=instances)
            saving_form = SavingSerifForm()
            
        elif mode == 'write':
            post_data = request.POST
            saving_action_list = SavingSerifAPI.get_head_list(user)
            
            saving_form = SavingSerifForm(post_data)
            saving_form.fields['saving_id'].choices = saving_action_list
            
            formset = ContinueSerifFormSet(post_data, queryset=instances)
                
            if saving_form.is_valid() and formset.is_valid():
                is_over = SavingSerifAPI.update_saved_action(request, formset, saving_form.cleaned_data)
                if is_over:
                    return SimpleError(request, u'これ以上のセリフセットを登録できません。')
                saving_form = SavingSerifForm()
        else:
            formset = ContinueSerifFormSet(request.POST, queryset=instances)
            
            if formset.is_valid():
#                ContinueSerifAPI.update_continue_serif(request, formset)
#                return HttpResponseRedirect(reverse('continue_serif_complete'))
                request.session['datas'] = formset.save(commit=False)
                return HttpResponseRedirect(reverse('continue_serif_confirm'))
            print formset.errors
            saving_form = SavingSerifForm()
    else:
        if 'datas' in request.session and isinstance(request.session['datas'], list) and request.session['datas'] and isinstance(request.session['datas'][0], ContinueSerif):
            datas = request.session['datas']
            ContinueSerifFormSetReload = modelformset_factory(ContinueSerif, form=ContinueSerifForm, extra=len(datas), can_delete=True)
            data_dicts = []
            for data in datas:
                data_dicts.append(model_to_dict(data))
            formset = ContinueSerifFormSetReload(queryset=instances.none(), initial=data_dicts)
        else:
            if 'datas' in request.session:
                del request.session['datas']
            basic_list = ContinueSerifAPI.get(user.id)
            if basic_list:
                formset = ContinueSerifFormSet(queryset=instances)
            else:
                character_serifs = CharacterSerifAPI.get_chices_list(user)
                ContinueSerifFormSetInitial = modelformset_factory(ContinueSerif, form=ContinueSerifForm, extra=len(character_serifs)+1)
                if character_serifs:
                    for serif in character_serifs:
                        serif['serif_text'] = serif['serif_text'].replace(u'<br />', u'\n')
                    formset = ContinueSerifFormSetInitial(queryset=instances, initial=character_serifs)
                else:
                    formset = ContinueSerifFormSetInitial(queryset=instances)
        saving_form = SavingSerifForm()
    
    saving_form.fields['saving_id'].choices = SavingSerifAPI.get_head_list(user)
    
    situation_list = SituationAPI.get_choices_list()
        
    skill_list = CharacterHaveSkillAPI.get_using(user)
    
    ctxt = RequestContext(request,{
            'formset': formset,
            'skill_list': skill_list,
            'situation_list': situation_list,
            'saving_form': saving_form,
            'character_serifs': character_serifs,
                                   })
    return render_to_response('regist/continue_serif/index.html', ctxt)

@login_required
@check_registration
@having_character
def confirm(request):
    """
    登録ページ 確認
    """
    if not 'datas' in request.session or not isinstance(request.session['datas'], list) or not isinstance(request.session['datas'][0], ContinueSerif):
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
    
    user = request.user
    
    datas = request.session['datas']
    
    ctxt = RequestContext(request,{
            'user': user,
            'datas': datas,
                                   })
    return render_to_response('regist/continue_serif/confirm.html', ctxt)

@login_required
@require_POST
@check_registration
@having_character
def execute(request):
    """
    登録ページ 実行
    """
    if not 'datas' in request.session or not isinstance(request.session['datas'], list) or not isinstance(request.session['datas'][0], ContinueSerif):
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
    
    datas = request.session['datas']
    
    ContinueSerifAPI.update_continue_serif(request, datas)
    del request.session['datas']
    return HttpResponseRedirect(reverse('continue_serif_complete'))

@login_required
@check_registration
@having_character
def complete(request):
    """
    登録ページ 完了
    """
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('regist/continue_serif/complete.html', ctxt)



# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import simplejson

from library.simple_error import SimpleError

from module.regist.continue_main.form import ContinueMainForm
from module.regist.continue_main.api import ContinueMainAPI
from module.regist.continue_main.models import ContinueMain

from module.master.quest.api import QuestAPI, MarkAPI
from module.character.api import CharacterBattleAPI, CharacterHaveItemAPI, CharacterAPI
from module.master.skill.api import SkillGetListAPI

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
    
    character_battle = CharacterBattleAPI.get(user)
    is_private_skill = False
    if character_battle and character_battle.levelup_point > 0:
        is_private_skill = True

    instance = ContinueMainAPI.get(user.id)
        
    if request.method == 'POST':
        if instance:
            form = ContinueMainForm(request.POST, instance=instance)
        else:
            form = ContinueMainForm(request.POST)
        quest_id = request.POST.get('quest_id', 0)
        if quest_id.isdigit():
            quest_id = int(quest_id)
        else:
            quest_id = 0
        
        form.fields['quest_id'].choices = QuestAPI.get_choices_list(user)
        form.fields['mark_id'].choices = MarkAPI.get_choices_list(quest_id, user)
        if form.is_valid():
            #ContinueMainAPI.update_continue_main(request, form)
            #return HttpResponseRedirect(reverse('continue_main_complete'))
            request.session['data'] = form.save(commit=False)
            return HttpResponseRedirect(reverse('continue_main_confirm'))
    else:
        if 'data' in request.session and isinstance(request.session['data'], ContinueMain):
            data = request.session['data']
            try:
                form = ContinueMainForm(instance=data)
            except:
                del request.session['data']
                form = ContinueMainForm()
        else:
            if instance:
                form = ContinueMainForm(instance=instance)
            else:
                form = ContinueMainForm()
        form.fields['quest_id'].choices = QuestAPI.get_choices_list(user)
        if instance:
            form.fields['mark_id'].choices = MarkAPI.get_choices_list(instance.quest_id, user)
        else:
            form.fields['mark_id'].choices = MarkAPI.get_choices_list(0, user)
        
    skill_list = SkillGetListAPI.get_selection_list(user)
    
    having_item_list = CharacterHaveItemAPI.get_filter(user)
    
    ctxt = RequestContext(request,{
            'form': form,
            'is_private_skill': is_private_skill,
            'skill_list': skill_list,
            'having_item_list': having_item_list,
                                   })
    return render_to_response('regist/continue_main/index.html', ctxt)

@login_required
@check_registration
@having_character
def confirm(request):
    """
    登録ページ 確認
    """
    user = request.user
    
    if not 'data' in request.session or not isinstance(request.session['data'], ContinueMain):
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
    
    data = request.session['data']
    character = CharacterAPI.get(user)
    
    data.user = user
    
    character_battle = CharacterBattleAPI.get(user)
    is_private_skill = False
    if character_battle and character_battle.levelup_point > 0:
        is_private_skill = True
    
    ctxt = RequestContext(request,{
            'data': data,
            'character': character,
            'is_private_skill': is_private_skill,
                                   })
    return render_to_response('regist/continue_main/confirm.html', ctxt)

@login_required
@require_POST
@check_registration
@having_character
def execute(request):
    """
    登録ページ 実行
    """
    if not 'data' in request.session or not isinstance(request.session['data'], ContinueMain):
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
    
    data = request.session['data']
    
    ContinueMainAPI.update_continue_main(request, data)
    del request.session['data']
    return HttpResponseRedirect(reverse('continue_main_complete'))

@login_required
@check_registration
@having_character
def complete(request):
    """
    登録ページ 完了
    """
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('regist/continue_main/complete.html', ctxt)

def select_mark(request, quest_id):
    """
    マークの判定
    """
    user = request.user
    quest_id = int(quest_id)
    
    mark_list = MarkAPI.get_choices_list(quest_id, user)
    
    ctxt = {
        "marklist": mark_list,
        "weathers": MarkAPI.get_weather_list(mark_list, user),
    }
    
    result = simplejson.dumps(ctxt, ensure_ascii=False)
    return HttpResponse(result, mimetype='text/javascript')



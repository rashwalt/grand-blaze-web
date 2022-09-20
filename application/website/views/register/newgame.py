# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect

from library.simple_error import SimpleError

from module.regist.newgame.form import NewGameForm
from module.regist.newgame.api import NewGameAPI

from module.master.install.api import InstallAPI
from module.master.race.api import RaceAPI

from module.account.api import UserProfileAPI

from module.master.management.decorators import check_registration
from module.character.decorators import havingd_character

@check_registration
@havingd_character
def index(request):
    """
    新規登録ページ インデックス
    """

    if request.method == 'POST':
        form = NewGameForm(request.POST)
        form.fields['install_class_id'].choices = InstallAPI.get_choices_list()
        form.fields['race_id'].choices = RaceAPI.get_choices_list()
        if form.is_valid():
            is_create = NewGameAPI.create_user_and_newgame(request, form)
            if not is_create:
                return SimpleError(request, u'すでに登録されています。メールボックスを確認し、仮登録を完了させて下さい。')
            return HttpResponseRedirect(reverse('newgame_complete'))
    else:
        form = NewGameForm()
        form.fields['install_class_id'].choices = InstallAPI.get_choices_list()
        form.fields['race_id'].choices = RaceAPI.get_choices_list()
    
    ctxt = RequestContext(request,{
            'form': form,
                                   })
    return render_to_response('regist/newgame/index.html', ctxt)

@check_registration
@havingd_character
def complete(request):
    """
    新規登録ページ 完了
    """
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('regist/newgame/complete.html', ctxt)

@check_registration
@havingd_character
def compare(request, activate_hash):
    """
    新規登録ページ メールハッシュ確認
    """
    target_user = UserProfileAPI.check_and_get_active_records(activate_hash)
    
    if not target_user:
        return SimpleError(request, u'有効期限が切れているか、または不正なアクセスです。再度、新規登録をやり直してください。')
    
    NewGameAPI.compare_newgame(request, target_user)
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('regist/newgame/complete_compare.html', ctxt)


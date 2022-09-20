# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect

from module.master.management.api import ManagementAPI
from module.character.api import CharacterAPI

def index(request):
    """
    登録ページ インデックス
    """
    site_manager = ManagementAPI.get()
    character = CharacterAPI.get(request.user)
    if site_manager.is_regist_stop and not character:
        return HttpResponseRedirect(reverse('newgame_index'))

    ctxt = RequestContext(request,{
                    'page_title': u'各種登録',
                                   })
    return render_to_response('regist/regist_index.html', ctxt)

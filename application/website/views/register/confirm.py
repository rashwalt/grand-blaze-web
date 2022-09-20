# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from module.regist.confirm.api import ConfirmAPI

from module.master.management.decorators import check_registration
from module.character.decorators import having_character

@login_required
@check_registration
@having_character
def index(request):
    """
    確認ページ インデックス
    """
    if request.method == 'POST':
        ConfirmAPI.send_mail(request)
        return HttpResponseRedirect(reverse('continue_confirm_complete'))
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('regist/confirm/index.html', ctxt)

@login_required
@check_registration
@having_character
def complete(request):
    """
    確認ページ 完了
    """
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('regist/confirm/complete.html', ctxt)



# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from library.simple_error import SimpleError

from module.bazzer.form import BazzerSearchForm, BazzerSellForm

from module.bazzer.api import BazzerAPI

from module.master.item.api import ItemTypeAPI

from module.character.api import CharacterHaveItemAPI

@login_required
def bazzer_list(request):
    """
    バザー出品物リスト
    """
    bazzer_list = []
    is_result = False

    if request.method == 'POST':
        form = BazzerSearchForm(request.POST)
        form.fields['type'].choices = ItemTypeAPI.get_choice_list()
        if form.is_valid():
            bazzer_list = BazzerAPI.search(request, form.cleaned_data)
            is_result = True
    else:
        form = BazzerSearchForm()
        form.fields['type'].choices = ItemTypeAPI.get_choice_list()

    ctxt = RequestContext(request,{
            'form': form,
            'bazzer_list': bazzer_list,
            'is_result': is_result,
                                   })
    return render_to_response('bazzer/index.html', ctxt)

@login_required
def detail(request, bazzer_id):
    """
    バザーの詳細
    """
    bazzer_data = BazzerAPI.get(bazzer_id)
    
    baz_history = BazzerAPI.get_item_history_list(bazzer_data.item_id)
    
    ctxt = RequestContext(request,{
            'bazzer_id': bazzer_id,
            'item_data': bazzer_data,
            'baz_history': baz_history,
                                   })
    return render_to_response('bazzer/detail.html', ctxt)

@login_required
def sell_register(request):
    """
    バザーの出品
    """
    user = request.user
    
    if request.method == 'POST':
        form = BazzerSellForm(request.POST)
        if form.is_valid():
            bazzer_id, error_message = BazzerAPI.create(request, form.cleaned_data)
            if bazzer_id < 0:
                return SimpleError(request, error_message)
            return HttpResponseRedirect(reverse('bazzer_sell_complete', args=[bazzer_id]))
    else:
        form = BazzerSellForm()

    having_item_list = CharacterHaveItemAPI.get_filter(user)
    
    ctxt = RequestContext(request,{
            'form': form,
            'having_item_list': having_item_list,
                                   })
    return render_to_response('bazzer/sell_register.html', ctxt)

@login_required
def sell_complete(request, bazzer_id):
    """
    バザーの出品完了
    """
    bazzer_id = int(bazzer_id)
    
    ctxt = RequestContext(request,{
            'bazzer_id': bazzer_id,
                                   })
    return render_to_response('bazzer/sell_complete.html', ctxt)

@login_required
def buy(request, bazzer_id):
    """
    バザーの購入
    """
    if request.method == 'POST':
        is_buy = BazzerAPI.buy(request, bazzer_id)
        if not is_buy:
            return SimpleError(request, u'落札できませんでした。すでに落札されたかキャンセルされたようです。')
    else:
        return SimpleError(request, u'落札できませんでした。再度検索しなおしてください。')
    
    return HttpResponseRedirect(reverse('bazzer_buy_complete', args=[bazzer_id]))

@login_required
def buy_complete(request, bazzer_id):
    """
    バザーの購入完了
    """
    bazzer_data = BazzerAPI.get(bazzer_id)
    
    ctxt = RequestContext(request,{
            'bazzer_id': bazzer_id,
            'item_data': bazzer_data,
                                   })
    return render_to_response('bazzer/buy_complete.html', ctxt)

@login_required
def cancel(request, bazzer_id):
    """
    バザーのキャンセル
    """
    is_buy = BazzerAPI.cancel(request, bazzer_id)
    if not is_buy:
        return SimpleError(request, u'キャンセルできませんでした。すでに落札されたかキャンセル権限がないようです。')
    
    return HttpResponseRedirect(reverse('bazzer_cancel_complete', args=[bazzer_id]))

@login_required
def cancel_complete(request, bazzer_id):
    """
    バザーのキャンセル完了
    """
    bazzer_data = BazzerAPI.get(bazzer_id)
    
    ctxt = RequestContext(request,{
            'bazzer_id': bazzer_id,
            'item_data': bazzer_data,
                                   })
    return render_to_response('bazzer/cancel_complete.html', ctxt)
    
#TODO: キャンセル


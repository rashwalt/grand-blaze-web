# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict
from django.utils import simplejson

from library.simple_error import SimpleError

from module.regist.continue_trade.models import ContinueTrade, ContinueShopping
from module.regist.continue_trade.form import ContinueShoppingFormSet, ContinueShoppingFormSetInitial, ContinueTradeFormSet, ContinueTradeFormSetInitial
from module.regist.continue_trade.api import ContinueTradeAPI, ContinueShoppingAPI

from module.character.api import CharacterHaveItemAPI, CharacterAPI

from module.master.item.api import ItemAPI

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

    instance_trade_items = ContinueTradeAPI.get_query_trade_item(user.id)
    instance_trade_moneys = ContinueTradeAPI.get_query_trade_money(user.id)
    instance_shop_sells = ContinueShoppingAPI.get_query_sell(user.id)
    instance_shop_buys = ContinueShoppingAPI.get_query_buy(user.id)
        
    if request.method == 'POST':
        post_data = request.POST
        sell_shop_formset = ContinueShoppingFormSet(post_data, queryset=instance_shop_sells, prefix='sell')
        buy_shop_formset = ContinueShoppingFormSet(post_data, queryset=instance_shop_buys, prefix='buy')
        tradeitem_formset = ContinueTradeFormSet(post_data, queryset=instance_trade_items, prefix='item')
        trademoney_formset = ContinueTradeFormSet(post_data, queryset=instance_trade_moneys, prefix='money')
        
        if sell_shop_formset.is_valid() and buy_shop_formset.is_valid() and tradeitem_formset.is_valid() and trademoney_formset.is_valid():
#            ContinueTradeAPI.update_continue_trade(request, tradeitem_formset, trademoney_formset, sell_shop_formset, buy_shop_formset)
#            return HttpResponseRedirect(reverse('continue_trade_complete'))
            request.session['sell_datas'] = sell_shop_formset.save(commit=False)
            request.session['buy_datas'] = buy_shop_formset.save(commit=False)
            request.session['item_datas'] = tradeitem_formset.save(commit=False)
            request.session['money_datas'] = trademoney_formset.save(commit=False)
            return HttpResponseRedirect(reverse('continue_trade_confirm'))
    else:
        if 'sell_datas' in request.session and isinstance(request.session['sell_datas'], list) and request.session['sell_datas'] and isinstance(request.session['sell_datas'][0], ContinueShopping) and \
        'buy_datas' in request.session and isinstance(request.session['buy_datas'], list) and request.session['buy_datas'] and isinstance(request.session['buy_datas'][0], ContinueShopping) and \
        'item_datas' in request.session and isinstance(request.session['item_datas'], list) and request.session['item_datas'] and isinstance(request.session['item_datas'][0], ContinueTrade) and \
        'money_datas' in request.session and isinstance(request.session['money_datas'], list) and request.session['money_datas'] and isinstance(request.session['money_datas'][0], ContinueTrade):
            sell_datas = request.session['sell_datas']
            data_dicts_sell = []
            for data in sell_datas:
                data_dicts_sell.append(model_to_dict(data))
            buy_datas = request.session['buy_datas']
            data_dicts_buy = []
            for data in buy_datas:
                data_dicts_buy.append(model_to_dict(data))
            item_datas = request.session['item_datas']
            data_dicts_item = []
            for data in item_datas:
                data_dicts_item.append(model_to_dict(data))
            money_datas = request.session['money_datas']
            data_dicts_money = []
            for data in money_datas:
                data_dicts_money.append(model_to_dict(data))

            sell_shop_formset = ContinueShoppingFormSet(queryset=instance_shop_sells.none(), initial=data_dicts_sell, prefix='sell')
            buy_shop_formset = ContinueShoppingFormSet(queryset=instance_shop_buys.none(), initial=data_dicts_buy, prefix='buy')
            tradeitem_formset = ContinueTradeFormSet(queryset=instance_trade_items, initial=data_dicts_item, prefix='item')
            trademoney_formset = ContinueTradeFormSet(queryset=instance_trade_moneys, initial=data_dicts_money, prefix='money')
        else:
            if 'datas' in request.session:
                del request.session['datas']
            basic_list = ContinueTradeAPI.get(user.id)
            if basic_list:
                sell_shop_formset = ContinueShoppingFormSet(queryset=instance_shop_sells, prefix='sell')
                buy_shop_formset = ContinueShoppingFormSet(queryset=instance_shop_buys, prefix='buy')
                tradeitem_formset = ContinueTradeFormSet(queryset=instance_trade_items, prefix='item')
                trademoney_formset = ContinueTradeFormSet(queryset=instance_trade_moneys, prefix='money')
            else:
                sell_shop_formset = ContinueShoppingFormSetInitial(queryset=instance_shop_sells, prefix='sell')
                buy_shop_formset = ContinueShoppingFormSetInitial(queryset=instance_shop_buys, prefix='buy')
                tradeitem_formset = ContinueTradeFormSetInitial(queryset=instance_trade_items, prefix='item')
                trademoney_formset = ContinueTradeFormSetInitial(queryset=instance_trade_moneys, prefix='money')
    
    having_item_list = CharacterHaveItemAPI.get_filter(user)
    
    item_list = ItemAPI.get_by_category(2)
    
    ctxt = RequestContext(request,{
            'sell_shop_formset': sell_shop_formset,
            'buy_shop_formset': buy_shop_formset,
            'tradeitem_formset': tradeitem_formset,
            'trademoney_formset': trademoney_formset,
            'having_item_list': having_item_list,
            'item_list': item_list,
            'chara': CharacterAPI.get(user),
                                   })
    return render_to_response('regist/continue_trade/index.html', ctxt)

@login_required
@check_registration
@having_character
def confirm(request):
    """
    登録ページ 確認
    """
    if not 'sell_datas' in request.session or not 'buy_datas' in request.session or not 'item_datas' in request.session or not 'money_datas' in request.session:
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
    
    user = request.user
    
    sell_datas = request.session['sell_datas']
    buy_datas = request.session['buy_datas']
    item_datas = request.session['item_datas']
    money_datas = request.session['money_datas']
    
    for data in sell_datas:
        data.user = user
    for data in buy_datas:
        data.user = user
    for data in item_datas:
        data.user = user
    for data in money_datas:
        data.user = user
        
    if len(sell_datas) < 5:
        for i in range(len(sell_datas), 5):
            sell_datas.append({})
    if len(buy_datas) < 5:
        for i in range(len(buy_datas), 5):
            buy_datas.append({})
    if len(item_datas) < 5:
        for i in range(len(item_datas), 5):
            item_datas.append({})
    if len(money_datas) < 5:
        for i in range(len(money_datas), 5):
            money_datas.append({})
    
    
    ctxt = RequestContext(request,{
            'user': user,
            'sell_datas': sell_datas,
            'buy_datas': buy_datas,
            'item_datas': item_datas,
            'money_datas': money_datas,
                                   })
    return render_to_response('regist/continue_trade/confirm.html', ctxt)

@login_required
@require_POST
@check_registration
@having_character
def execute(request):
    """
    登録ページ 実行
    """
    if not 'sell_datas' in request.session or not 'buy_datas' in request.session or not 'item_datas' in request.session or not 'money_datas' in request.session:
        return SimpleError(request, u'登録を行おうとしている内容を取得できませんでした。再度はじめからご登録下さい。') 
        
    sell_datas = request.session['sell_datas']
    buy_datas = request.session['buy_datas']
    item_datas = request.session['item_datas']
    money_datas = request.session['money_datas']
    
    ContinueTradeAPI.update_continue_trade(request, item_datas, money_datas, sell_datas, buy_datas)
    del request.session['sell_datas']
    del request.session['buy_datas']
    del request.session['item_datas']
    del request.session['money_datas']
    return HttpResponseRedirect(reverse('continue_trade_complete'))

@login_required
@check_registration
@having_character
def complete(request):
    """
    継続登録ページ 完了
    """
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('regist/continue_trade/complete.html', ctxt)

def item_data(request, category_id):
    """
    アイテム取得
    """
    user = request.user
    
    item_list = ItemAPI.get_by_category(category_id)
    
    for row in item_list:
        row['it_price'] = float(row['it_price'])
    
    ctxt = {
        "itemlist": item_list,
    }
    
    result = simplejson.dumps(ctxt, ensure_ascii=False)
    return HttpResponse(result, mimetype='text/javascript')



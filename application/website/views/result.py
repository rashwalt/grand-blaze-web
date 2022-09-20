# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext, TemplateDoesNotExist
from django.template.loader import find_template
from django.http import Http404

from module.result.form import CharacterSearchForm

from module.character.api import CharacterAPI

def search(request):
    """
    キャラクター検索
    """

    article_list = []
    is_result = False

    if request.method == 'POST':
        form = CharacterSearchForm(request.POST)
        if form.is_valid():
            article_list = CharacterAPI.search(request, form.cleaned_data)
            is_result = True
    else:
        form = CharacterSearchForm()

    ctxt = RequestContext(request,{
            'form': form,
            'article_list': article_list,
            'is_result': is_result,
                                   })
    return render_to_response('result/search.html', ctxt)

def chara_list(request, page):
    """
    結果リスト
    """
    page = int(page)
    
    try:
        find_template('result/list%04d.html' % page)
    except TemplateDoesNotExist, err:
        raise Http404
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('result/list%04d.html' % page, ctxt)

def chara_com_list(request, page):
    """
    結果リスト(メッセージ)
    """
    page = int(page)
    
    try:
        find_template('result/lcom%04d.html' % page)
    except TemplateDoesNotExist, err:
        raise Http404
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('result/lcom%04d.html' % page, ctxt)


def private_status(request, entry):
    """
    プライベート結果
    """
    entry = int(entry)
    
    try:
        find_template('result/status/character%04d.html' % entry)
    except TemplateDoesNotExist, err:
        raise Http404
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('result/status/character%04d.html' % entry, ctxt)

def party_status(request, party):
    """
    パーティ結果
    """
    party = int(party)
    
    try:
        find_template('result/party/party%04d.html' % party)
    except TemplateDoesNotExist, err:
        raise Http404
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('result/party/party%04d.html' % party, ctxt)
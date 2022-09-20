# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from module.link.api import LinkAPI, LinkCategoryAPI
from module.link.form import LinkForm

def link_index(request):
    """
    リンクサイト
    """
    
    link_category_list = LinkCategoryAPI.get_category_list()
    
    link_list = []
    for link_category in link_category_list:
        row = {}
        row['data'] = LinkAPI.get_category_top(link_category.id)
        row['category_name'] = link_category.name
        row['category'] = link_category.id
        link_list.append(row)
    
    ctxt = RequestContext(request,{
            'link_list': link_list,
                                   })
    return render_to_response('link/index.html', ctxt)


@login_required
def register(request):
    """
    サイト登録ページ インデックス
    """
    user = request.user

    instance = LinkAPI.get(user.id)
        
    if request.method == 'POST':
        if instance:
            form = LinkForm(request.POST, instance=instance)
        else:
            form = LinkForm(request.POST)
        
        if form.is_valid():
            LinkAPI.update_link(request, form)
    else:
        if instance:
            form = LinkForm(instance=instance)
        else:
            form = LinkForm()
    
    ctxt = RequestContext(request,{
            'form': form,
                                   })
    return render_to_response('link/register.html', ctxt)
  



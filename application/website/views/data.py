# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.utils import simplejson

from library.pager import get_pager_from_list
from library.simple_error import SimpleError

from module.master.install.api import InstallAPI
from module.master.skill.api import SkillAPI, SkillCategoryAPI, SkillGetListAPI
from module.master.item.api import ItemAPI, ItemTypeAPI

CONVERT_WEAPONS = {
    1: 1,
    2: 2,
    3: 3,
    6: 4,
    8: 5,
    9: 6,
    10: 7,
    11: 8,
    12: 9,
    15: 10,
    16: 11,
    17: 12,
    19: 13,
    21: 14,
    23: 18,
    24: 15,
    25: 16,
    26: 17,
}


def install_data(request, install_id):
    """
    クラス習得スキル＆詳細
    """
    install_id = int(install_id)
    
    install_data = InstallAPI.get(install_id)
    install_skills = InstallAPI.get_install_skill(install_id)
    
    if not install_data:
        raise Http404
    
    ctxt = RequestContext(request,{
                'install_data': install_data,
                'install_skills': install_skills,
                                   })
    return render_to_response('data/install_data.html', ctxt)

def weapon_data(request, weapon_id):
    """
    クラス習得スキル＆詳細
    """
    weapon_id = int(weapon_id)
    
    if weapon_id > 32:
        raise Http404
    
    weapon_data = SkillCategoryAPI.get(weapon_id)
    weapon_skills = SkillAPI.get_list_by_type(weapon_id)
    
    item_type = ItemTypeAPI.get(CONVERT_WEAPONS[weapon_id])
    item_datas = ItemAPI.get_by_category(CONVERT_WEAPONS[weapon_id])
    
    if not weapon_data:
        raise Http404
    
    ctxt = RequestContext(request,{
                'weapon_data': weapon_data,
                'weapon_skills': weapon_skills,
                'item_type': item_type,
                'item_datas': item_datas,
                                   })
    return render_to_response('data/weapon_data.html', ctxt)

def protect_data(request, protect_id):
    """
    販売品防具リスト
    """
    protect_id = int(protect_id)
    
    if protect_id < 33 or protect_id > 41:
        raise Http404
    
    item_d = ItemTypeAPI.get(protect_id)
    item_datas = ItemAPI.get_by_category(protect_id)
    
    if not item_datas:
        raise Http404
    
    ctxt = RequestContext(request,{
                'item_d': item_d,
                'item_datas': item_datas,
                                   })
    return render_to_response('data/protect_data.html', ctxt)

def private_data(request):
    """
    プライベートスキル
    """
    
    private_skills = SkillGetListAPI.get_private_list()
    
    ctxt = RequestContext(request,{
                'private_skills': private_skills,
                                   })
    return render_to_response('data/private_data.html', ctxt)

def sell_data(request, category_id=2):
    """
    販売品一覧
    """
    category_id = int(category_id)
    
    item_d = ItemTypeAPI.get(category_id)
    item_list = ItemAPI.get_by_category(category_id)
    type_id = 1
    if category_id in [2, 3, 4, 5, 6, 7, 8]:
        type_id = 1
    elif category_id in [1, 9, 10, 11, 12, 13, 14]:
        type_id = 2
    elif category_id in [15, 16, 17, 18]:
        type_id = 3
    elif category_id in [33, 35, 36, 37, 38, 39, 40, 41]:
        type_id = 4
    elif category_id in [53, 54, 55, 56, 57, 58, 64, 65, 66]:
        type_id = 5
    elif category_id in [49, 63]:
        type_id = 6
    else:
        raise Http404
    
    ctxt = RequestContext(request,{
                'item_d': item_d,
                'item_list': item_list,
                'category_id': category_id,
                'type_id': type_id,
                                   })
    return render_to_response('data/sell_data.html', ctxt)

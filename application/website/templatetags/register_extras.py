# -*- coding: utf-8 -*-

from django import template
from django.core.urlresolvers import reverse

from module.regist.utils.preview_util import PreviewUtil

from module.party.api import PartyAPI
from module.master.battleaction.models import BattleTarget
from module.master.skill.models import Skill
from module.master.situation.models import Situation
from module.regist.constant import RegistConstant

register = template.Library()

import re

@register.assignment_tag
def partymember(str, request, counter):
    if not counter:
        return str
    counter = int(counter)
    user = request.user
    party_members = PartyAPI.get_party_member(user)
    
    party_length = len(party_members)
    dec_count = counter - 1
    
    party_member_name = u''
    if dec_count >= 0 and dec_count < party_length:
        party_member_name = party_members[dec_count].character.nick_name
    
    str = re.sub(r'<chara_name>', party_member_name, str)
    return str

@register.assignment_tag
def partymember_user(str, user, counter):
    if not counter:
        return str
    counter = int(counter)
    party_members = PartyAPI.get_party_member(user)
    
    party_length = len(party_members)
    dec_count = counter - 1
    
    party_member_name = u''
    if dec_count >= 0 and dec_count < party_length:
        party_member_name = party_members[dec_count].character.nick_name
    
    str = re.sub(r'<chara_name>', party_member_name, str)
    return str

@register.filter
def sub_money(money):
    if money < 1 and money > 0:
        return money
    else:
        return int(money)

@register.filter
def get_target_name(action, index):
    if index >= len(action):
        return ''
    target = BattleTarget.get(action[index]['action_target'])
    if target:
        return target.name
    return ''

@register.filter
def get_arts_name(action, index):
    if index >= len(action):
        return ''
    skill = Skill.get(action[index]['perks_id'])
    if skill:
        return skill.name
    return u''

@register.filter
def get_situaltion_name(action, index):
    if index >= len(action):
        return ''
    situation = Situation.get(action[index]['situation_id'])
    if situation:
        return situation.name
    return u''

@register.filter
def preview(word, user):
    preview_data = PreviewUtil(user)
    return preview_data.convert(word)
preview.is_safe = True

@register.filter
def previewlist(word, user):
    preview_data = PreviewUtil(user)
    return preview_data.convert(word, is_list=True)
previewlist.is_safe = True
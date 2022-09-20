# -*- coding: utf-8 -*-

import datetime
from django.conf import settings

from module.master.management.api import ManagementAPI
from module.account.api import InstantMessageAPI, UserProfileAPI
from module.character.api import CharacterAPI

def contexts(request):
    """
    コンテキストプロセッサ
    """
    user = request.user

    return {
            'request': request,
            'debug': settings.DEBUG,
            'publish_date': datetime.datetime.now().strftime('%Y%m%d'),
            'read_complete_count': InstantMessageAPI.get_read_complete_count(user),
            'character': CharacterAPI.get(user),
            'site_manager': ManagementAPI.get(),
            'user_name': UserProfileAPI.get_user_name(user) if user.is_authenticated() else '',
            }
    
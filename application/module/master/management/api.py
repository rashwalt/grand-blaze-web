# -*- coding: utf-8 -*-

from django.conf import settings

from module.master.management.models import Management

class ManagementAPI(object):
    @classmethod
    def get(cls):
        return Management.get(settings.SITE_MANAGER_ID)
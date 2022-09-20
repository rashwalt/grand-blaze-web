# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from module.master.management.api import ManagementAPI


def check_registration(view_func):
    def decorate(request, *args, **kwds):
        
        site_manager = ManagementAPI.get()
        if not site_manager.is_regist_stop:
            return HttpResponseRedirect(reverse('regist_index'))

        return view_func(request, *args, **kwds)
        decorate.__doc__ = view_func.__doc__
        decorate.__dict__ = view_func.__dict__
    return decorate

# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from module.character.api import CharacterAPI


def having_character(view_func):
    def decorate(request, *args, **kwds):
        
        character = CharacterAPI.get(request.user)
        if not character:
            return HttpResponseRedirect(reverse('newgame_index'))

        return view_func(request, *args, **kwds)
        decorate.__doc__ = view_func.__doc__
        decorate.__dict__ = view_func.__dict__
    return decorate

def havingd_character(view_func):
    def decorate(request, *args, **kwds):
        
        character = CharacterAPI.get(request.user)
        if character:
            return HttpResponseRedirect(reverse('regist_index'))

        return view_func(request, *args, **kwds)
        decorate.__doc__ = view_func.__doc__
        decorate.__dict__ = view_func.__dict__
    return decorate
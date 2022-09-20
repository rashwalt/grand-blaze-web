# -*- coding: utf-8 -*-

from os.path import getsize, getmtime

import datetime

from django import template
from django.conf import settings

from django.utils.encoding import force_unicode
import re

register = template.Library()

@register.filter
def intcomma(val):
    orig = force_unicode(val)
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', orig)
    if orig == new:
        return new
    else:
        return intcomma(new)
    

@register.filter
def get_size(str):
    
    size = int(getsize(settings.MEDIA_ROOT + str))
    return intcomma(size)
    

@register.filter
def get_time(str):
    
    tim = getmtime(settings.MEDIA_ROOT + str)
    dat = datetime.datetime.fromtimestamp(tim)
    return dat.strftime('%Y/%m/%d %H:%M:%S')


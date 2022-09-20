# -*- coding: utf-8 -*-

from django import template
from django.core.urlresolvers import reverse

register = template.Library()

import re

@register.filter
def urlconvert(str):
    str = re.sub(r'(https?:\/\/[\x21-\x7e]+)', r'<a href="\1">\1</a>', str)
    return str
urlconvert.is_safe=True


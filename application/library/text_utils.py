# -*- coding: utf-8 -*-

import re

HEADSTR = re.compile("^", re.MULTILINE)

class TextUtil(object):
    
    @classmethod
    def linebreaksreply(cls, text):
        if text:
            text = HEADSTR.sub("> ", text)
            return text
        else:
            return ''

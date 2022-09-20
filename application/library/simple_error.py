# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

def SimpleError(request, message):
    """
    単純エラー
    """
    
    ctxt = RequestContext(request,{
            'message': message,
                                   })
    return render_to_response('error/simple_error.html', ctxt)

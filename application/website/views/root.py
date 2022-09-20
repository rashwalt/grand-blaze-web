# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context, loader
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.conf import settings
from django.contrib.auth.decorators import login_required

from library.pager import get_pager_from_list
from library.send_mail import send_mail

from module.master.notice.api import NoticeAPI
from module.master.notice.constant import NoticeConstant

from module.support.form import SupportForm
from module.support.constant import SupportConstant

from module.account.api import UserProfileAPI
from module.master.management.api import ManagementAPI
from library.simple_error import SimpleError


def index(request):
    """
    サイトのインデックス（トップページ）
    """
    notice_list = NoticeAPI.get_top()
    topics_list = NoticeAPI.get_category_top(NoticeConstant.CATEGORY_TOPICS)
    site_manager = ManagementAPI.get()
    
    ctxt = RequestContext(request,{
            'notice_list': notice_list,
            'topics_list': topics_list,
            'site_manager': site_manager,
                                   })
    return render_to_response('root/index.html', ctxt)

def information(request):
    """
    インフォメーション記事リスト
    """
    
    information_list = []
    for category_id in (NoticeConstant.CATEGORY_IMPORTANT, NoticeConstant.CATEGORY_NORMAL, NoticeConstant.CATEGORY_VERSIONUP, NoticeConstant.CATEGORY_MAINTENANCE):
        row = {}
        row['data'] = NoticeAPI.get_active_category_top(category_id, limit=None)
        row['category_name'] = NoticeConstant.get_category_name(category_id)
        row['category'] = category_id
        information_list.append(row)
    
    ctxt = RequestContext(request,{
            'information_list': information_list,
                                   })
    return render_to_response('root/information_list.html', ctxt)

def category(request, category_id, page=1):
    """
    お知らせのカテゴリ別記事リスト
    """
    category_id = int(category_id)
    
    category_list = NoticeAPI.get_category_top(category_id, limit=None)
    
    pager, category_list = get_pager_from_list(category_list, limit=10, page=page)
    
    category_name = NoticeConstant.get_category_name(category_id)
    
    ctxt = RequestContext(request,{
            'pager': pager,
            'category_id': category_id,
            'category_name': category_name,
            'category_list': category_list,
                                   })
    return render_to_response('root/notice_category_list.html', ctxt)

def notice_detail(request, notice_id):
    """
    お知らせの詳細
    """
    notice_id = int(notice_id)
    
    detail_data = NoticeAPI.get(notice_id)
    
    if not detail_data or detail_data.category == NoticeConstant.CATEGORY_TOPICS:
        return SimpleError(request, u'このお知らせは表示できません。')
    
    ctxt = RequestContext(request,{
            'detail_data': detail_data,
                                   })
    return render_to_response('root/notice_detail.html', ctxt)

def support_index(request):
    """
    お問い合わせ
    """
    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            title = SupportConstant.get_subject_name(int(subject))
            subject = u"[Grand Blaze] : お問い合わせ - %s" % title
            
            mail_from =  form.cleaned_data['from_mail']
            name = form.cleaned_data['name']
            entry_no = form.cleaned_data['entry_no']
            body = form.cleaned_data['body']
            
            # 送信者情報
            ip_address = request.META.get('REMOTE_ADDR','')
            host = request.META.get('REMOTE_HOST', '')
            agent = request.META.get('HTTP_USER_AGENT','')
            
            mail_body = u"""
本メールはお問い合わせからの送信です。

送信者：
%s (E-No. %s)

お問い合わせ内容：
%s

%s

_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
IPアドレス : %s
ブラウザ : %s
ホスト名 : %s
_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
""" % (name, entry_no, title, body, ip_address, agent, host)
            
            # 送信
            send_mail(subject, mail_body, mail_from, [settings.MAIL_FROM])
            return HttpResponseRedirect(reverse('root_support_done'))
    else:
        initial_data = None
        user_profile = UserProfileAPI.get_user_profile(request)
        if user_profile:
            initial_data = {'name': user_profile.user_name, 'entry_no': request.user.id, 'from_mail': request.user.email}
        form = SupportForm(initial=initial_data)
    
    ctxt = RequestContext(request,{
            'form': form,
                                   })
    return render_to_response('root/support_index.html', ctxt)

def support_done(request):
    """
    サポート投稿完了
    """
    
    ctxt = RequestContext(request,{
                                   })
    return render_to_response('root/support_done.html', ctxt)

@login_required
def cache_clear(request):
    """
    キャッシュ削除
    """
    if request.user.is_staff:
        from django.core.cache import cache
        cache.clear()
    
    return HttpResponseRedirect(reverse('root_index'))

def server_error(request, template_name='500.html'):
    """
    500 error handler.

    Templates: `500.html`
    Context:
        MEDIA_URL
            Path of static media (e.g. "media.example.org")
    """
    t = loader.get_template(template_name) # You need to create a 500.html template.
    return HttpResponseServerError(t.render(Context({
        'MEDIA_URL': settings.MEDIA_URL
    })))
    
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import simplejson

from library.pager import get_pager_from_list
from library.simple_error import SimpleError

from module.forum.form import ThreadForm, ArticleForm, ArticleEditForm, ArticleDeleteForm, ThreadSearchForm, NotAuthThreadForm, NotAuthArticleForm

from module.forum.api import ForumAPI, ForumStatusAPI, ThreadAPI, ArticleAPI

from module.account.api import UserProfileAPI


def forum_index(request):
    """
    フォーラム一覧
    """
    
    lastest = ArticleAPI.lastest()
    
    ctxt = RequestContext(request,{
            'lastest_list': lastest,
                                   })
    return render_to_response('forum/forum_index.html', ctxt)

def forum_list(request, forum_id, page=1):
    """
    フォーラムリスト
    """
    forum_id = int(forum_id)

    forum = ForumAPI.get_forum(forum_id)
    
    forum_list = ForumAPI.get_thread_list(forum_id)
    
    pager, forum_list = get_pager_from_list(forum_list, limit=10, page=page)
    
    ctxt = RequestContext(request,{
            'pager': pager,
            'forum_list': forum_list,
            'forum': forum,
                                   })
    return render_to_response('forum/forum_list.html', ctxt)

@login_required
def thread_create(request, forum_id):
    """
    スレッドの作成
    """
    forum_id = int(forum_id)
    is_preview = False
    preview_data = {}

    if request.method == 'POST':
        posted_data = request.POST.copy()
        is_preview = request.POST.get('preview', False)
        posted_data['preview'] = False
        form = ThreadForm(posted_data)
        form.fields['forum_status'].choices = ForumStatusAPI.get_status_list(forum_id, request, is_create=True)
        if form.is_valid():
            if is_preview:
                preview_data['user'] = UserProfileAPI.get_user_name(request.user)
                preview_data['body'] = form.cleaned_data['body']
                preview_data['title'] = form.cleaned_data['title']
            else:
                ThreadAPI.create_thread(request, forum_id, form.cleaned_data)
                return HttpResponseRedirect(reverse('forum_list', args=[forum_id]))
    else:
        form = ThreadForm()
        form.fields['forum_status'].choices = ForumStatusAPI.get_status_list(forum_id, request, is_create=True)

    forum = ForumAPI.get_forum(forum_id)
    
    ctxt = RequestContext(request,{
            'forum': forum,
            'form': form,
            'is_preview': is_preview,
            'preview_data': preview_data,
                                   })
    return render_to_response('forum/thread_create.html', ctxt)

def thread_create_notauth(request, forum_id):
    """
    スレッドの作成(非認証用)
    """
    forum_id = int(forum_id)
    is_preview = False
    preview_data = {}
    
    forum = ForumAPI.get_forum(forum_id)
    
    # ログイン済ならリダイレクト
    if not forum.is_not_auth or request.user.is_authenticated():
        return HttpResponseRedirect(reverse('forum_thread_create', args=[forum_id]))

    if request.method == 'POST':
        posted_data = request.POST.copy()
        is_preview = request.POST.get('preview', False)
        posted_data['preview'] = False
        form = NotAuthThreadForm(posted_data)
        form.fields['forum_status'].choices = ForumStatusAPI.get_status_list(forum_id, request, is_create=True)
        if form.is_valid():
            if is_preview:
                preview_data['create_user_name'] = form.cleaned_data['create_user_name']
                preview_data['body'] = form.cleaned_data['body']
                preview_data['title'] = form.cleaned_data['title']
            else:
                ThreadAPI.create_thread(request, forum_id, form.cleaned_data)
                return HttpResponseRedirect(reverse('forum_list', args=[forum_id]))
    else:
        form = NotAuthThreadForm()
        form.fields['forum_status'].choices = ForumStatusAPI.get_status_list(forum_id, request, is_create=True)
    
    ctxt = RequestContext(request,{
            'forum': forum,
            'form': form,
            'is_preview': is_preview,
            'preview_data': preview_data,
                                   })
    return render_to_response('forum/thread_create_notauth.html', ctxt)

def thread_detail(request, forum_id, thread_id, page=1):
    """
    スレッド詳細
    """
    forum_id = int(forum_id)
    thread_id = int(thread_id)
    page = int(page)

    forum = ForumAPI.get_forum(forum_id)

    thread = ThreadAPI.get_thread(thread_id)

    article_list = ArticleAPI.get_article_list(thread_id)

    pager, article_list = get_pager_from_list(article_list, limit=10, page=page)

    ThreadAPI.update_view_count(thread_id)

    ctxt = RequestContext(request,{
        'forum': forum,
        'pager': pager,
        'thread': thread,
        'article_list': article_list,
        })
    return render_to_response('forum/thread_detail.html', ctxt)

@login_required
def thread_reply(request, forum_id, thread_id, article_id=0):
    """
    スレッドへの返信
    """
    forum_id = int(forum_id)
    thread_id = int(thread_id)
    article_id = int(article_id)

    forum = ForumAPI.get_forum(forum_id)
    thread = ThreadAPI.get_thread(thread_id)
    
    if thread.is_rock:
        return SimpleError(request, u'このスレッドに返信できません。')

    article_list = ArticleAPI.get_article_list(thread_id, is_last=True)
    is_preview = False
    preview_data = {}

    if request.method == 'POST':
        posted_data = request.POST.copy()
        is_preview = request.POST.get('preview', False)
        posted_data['preview'] = False
        form = ArticleForm(posted_data)
        form.fields['forum_status'].choices = ForumStatusAPI.get_status_list(forum_id, request, is_lock=True)
        if form.is_valid():
            if is_preview:
                preview_data['user'] = UserProfileAPI.get_user_name(request.user)
                preview_data['body'] = form.cleaned_data['body']
            else:
                ArticleAPI.post_article(request, forum_id, thread_id, form.cleaned_data)
                return HttpResponseRedirect(reverse('forum_thread_detail', args=[forum_id, thread_id]))
    else:
        article_body = ''
        if article_id:
            # 引用
            article = ArticleAPI.get(article_id)
            article_body = article.body
            if article_body:
                article_body = '> ' + article_body.replace('\n', '\n> ')
        form = ArticleForm()
        form.fields['forum_status'].choices = ForumStatusAPI.get_status_list(forum_id, request, is_lock=True)
        form.fields['body'].initial = article_body
        form.fields['forum_status'].initial = thread.forum_status_id
    
    ctxt = RequestContext(request,{
            'forum': forum,
            'form': form,
            'thread': thread,
            'article_list': article_list,
            'is_preview': is_preview,
            'preview_data': preview_data,
                                   })
    return render_to_response('forum/thread_reply.html', ctxt)

def thread_reply_notauth(request, forum_id, thread_id, article_id=0):
    """
    スレッドへの返信
    """
    forum_id = int(forum_id)
    thread_id = int(thread_id)
    article_id = int(article_id)
    forum = ForumAPI.get_forum(forum_id)
    
    # ログイン済ならリダイレクト
    if not forum.is_not_auth or request.user.is_authenticated():
        if article_id:
            return HttpResponseRedirect(reverse('forum_thread_reply', args=[forum_id, thread_id, article_id]))
        else:
            return HttpResponseRedirect(reverse('forum_thread_reply', args=[forum_id, thread_id]))

    thread = ThreadAPI.get_thread(thread_id)
    
    if thread.is_rock:
        return SimpleError(request, u'このスレッドに返信できません。')

    article_list = ArticleAPI.get_article_list(thread_id, is_last=True)
    is_preview = False
    preview_data = {}

    if request.method == 'POST':
        posted_data = request.POST.copy()
        is_preview = request.POST.get('preview', False)
        posted_data['preview'] = False
        form = NotAuthArticleForm(posted_data)
        form.fields['forum_status'].choices = ForumStatusAPI.get_status_list(forum_id, request, is_lock=True)
        if form.is_valid():
            if is_preview:
                preview_data['user_name'] = form.cleaned_data['user_name']
                preview_data['body'] = form.cleaned_data['body']
            else:
                ArticleAPI.post_article(request, forum_id, thread_id, form.cleaned_data)
                return HttpResponseRedirect(reverse('forum_thread_detail', args=[forum_id, thread_id]))
    else:
        article_body = ''
        if article_id:
            # 引用
            article = ArticleAPI.get(article_id)
            article_body = article.body
            if article_body:
                article_body = '> ' + article_body.replace('\n', '\n> ')
        form = NotAuthArticleForm()
        form.fields['forum_status'].choices = ForumStatusAPI.get_status_list(forum_id, request, is_lock=True)
        form.fields['body'].initial = article_body
        form.fields['forum_status'].initial = thread.forum_status_id
    
    ctxt = RequestContext(request,{
            'forum': forum,
            'form': form,
            'thread': thread,
            'article_list': article_list,
            'is_preview': is_preview,
            'preview_data': preview_data,
                                   })
    return render_to_response('forum/thread_reply_notauth.html', ctxt)

@login_required
def article_edit(request, forum_id, thread_id, article_id):
    """
    レスの編集
    """
    forum_id = int(forum_id)
    thread_id = int(thread_id)
    article_id = int(article_id)

    forum = ForumAPI.get_forum(forum_id)
    thread = ThreadAPI.get_thread(thread_id)
    article = ArticleAPI.get(article_id)
    
    if thread.is_rock:
        return SimpleError(request, u'このスレッドは編集できません。')

    if article.is_delete:
        return SimpleError(request, u'この記事は削除されているため、編集できません。')

    if article.user_id != request.user.id:
        return SimpleError(request, u'この記事は自分の書いた記事ではないため、編集できません。')

    article_list = ArticleAPI.get_article_list(thread_id, is_last=True)
    is_preview = False
    preview_data = {}

    if request.method == 'POST':
        posted_data = request.POST.copy()
        is_preview = request.POST.get('preview', False)
        posted_data['preview'] = False
        form = ArticleEditForm(posted_data)
        if form.is_valid():
            if is_preview:
                preview_data['user'] = UserProfileAPI.get_user_name(request.user)
                preview_data['body'] = form.cleaned_data['body']
                preview_data['edit_mean'] = form.cleaned_data['edit_mean']
            else:
                ArticleAPI.update_article(request, article_id, form.cleaned_data)
                return HttpResponseRedirect(reverse('forum_thread_detail', args=[forum_id, thread_id]))
    else:
        form = ArticleEditForm()
        form.fields['body'].initial = article.body

    ctxt = RequestContext(request,{
            'forum': forum,
            'form': form,
            'thread': thread,
            'article': article,
            'article_list': article_list,
            'is_preview': is_preview,
            'preview_data': preview_data,
                                   })
    return render_to_response('forum/article_edit.html', ctxt)

@login_required
def article_delete(request, forum_id, thread_id, article_id):
    """
    レスの削除
    """
    forum_id = int(forum_id)
    thread_id = int(thread_id)
    article_id = int(article_id)

    forum = ForumAPI.get_forum(forum_id)
    thread = ThreadAPI.get_thread(thread_id)
    article = ArticleAPI.get(article_id)
    
    user = request.user
    
    if thread.is_rock:
        return SimpleError(request, u'このスレッドは削除できません。')

    if article.is_delete:
        return SimpleError(request, u'この記事はすでに削除されています。')

    if article.user_id != user.id and not user.is_staff:
        return SimpleError(request, u'この記事は自分の書いた記事ではないため、削除できません。')

    if request.method == 'POST':
        form = ArticleDeleteForm(request.POST)
        if form.is_valid():
            ArticleAPI.delete_article(request, article_id, form.cleaned_data)
            return HttpResponseRedirect(reverse('forum_thread_detail', args=[forum_id, thread_id]))
    else:
        form = ArticleDeleteForm()

    ctxt = RequestContext(request,{
            'forum': forum,
            'form': form,
            'thread': thread,
            'article': article,
            'user_name': UserProfileAPI.get_user_name(request.user),
                                   })
    return render_to_response('forum/article_delete.html', ctxt)

def search(request):
    """
    スレッドの検索
    """

    article_list = []
    is_result = False

    if request.method == 'POST':
        form = ThreadSearchForm(request.POST)
        form.fields['forum_id'].choices = ForumAPI.get_forum_choice_list_and_none()
        if form.is_valid():
            if not form.cleaned_data['body']:
                return SimpleError(request, u'検索語句が指定されていません。')
            article_list = ArticleAPI.search(request, form.cleaned_data)
            is_result = True
    else:
        form = ThreadSearchForm()
        form.fields['forum_id'].choices = ForumAPI.get_forum_choice_list_and_none()

    ctxt = RequestContext(request,{
            'form': form,
            'article_list': article_list,
            'is_result': is_result,
                                   })
    return render_to_response('forum/search.html', ctxt)

def so_good(request, article_id):
    """
    Ajax いいね
    """
    article_id = int(article_id)
    good_count = 0
    
    if hasattr(request, 'user'):
        user = request.user
        good_count = ArticleAPI.update_good_count(article_id, user)
    
    ctxt = {
        "goodcount": good_count,
        "article_id": article_id,
    }
    
    result = simplejson.dumps(ctxt, ensure_ascii=False)
    return HttpResponse(result, mimetype='text/javascript')

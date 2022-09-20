# -*- coding: utf-8 -*-

import datetime

from module.forum.models import Forum, ForumStatus, Thread, Article

class ForumAPI(object):
    
    @classmethod
    def get_forum_list(cls):
        return Forum.get_forum_list()

    @classmethod
    def get_forum(cls, forum_id):
        return Forum.get(forum_id)

    @classmethod
    def get_thread_list(cls, forum_id):
        return Thread.get_thread_list(forum_id)

    @classmethod
    def get_forum_choice_list_and_none(cls):
        forum_list =  Forum.get_forum_choice_list()
        forum_list.insert(0, (0, u'すべて'))
        return forum_list

class ForumStatusAPI(object):
    
    @classmethod
    def get(cls, status_id):
        return ForumStatus.get(status_id)
    
    @classmethod
    def get_status_list(cls, forum_id, request, is_create=False, is_lock=False):
        return ForumStatus.get_status_list( forum_id, request, is_create, is_lock)

    @classmethod
    def get_name(cls, forum_status_id):
        fortum_status = ForumStatus.get(forum_status_id)
        return fortum_status.name

class ThreadAPI(object):
    
    @classmethod
    def create_thread(cls, request, forum_id, cleaned_data):
        title = cleaned_data['title']
        body = cleaned_data['body']
        forum_status = int(cleaned_data['forum_status'])
        
        if 'status_change_pass' in cleaned_data:
            create_user_name = cleaned_data['create_user_name']
            status_change_pass = cleaned_data['status_change_pass']
            thread = Thread.objects.create(forum_id=forum_id, title=title, create_user_id=0, create_user_name=create_user_name, is_rock=False, thread_solid=False, forum_status_id=forum_status, status_change_pass=status_change_pass, last_article_update_at=datetime.datetime.now())
            thread.save()
        
            article = Article.objects.create(forum_id=forum_id, thread=thread, body=body, user_id=0, user_name=create_user_name)
            article.save()
        else:
            is_rock = cleaned_data['is_rock']
            thread_solid = cleaned_data['thread_solid']
            thread = Thread.objects.create(forum_id=forum_id, title=title, create_user_id=request.user.id, is_rock=is_rock, thread_solid=thread_solid, forum_status_id=forum_status, last_article_update_at=datetime.datetime.now())
            thread.save()
        
            article = Article.objects.create(forum_id=forum_id, thread=thread, body=body, user_id=request.user.id)
            article.save()

    @classmethod
    def get_thread(cls, thread_id):
        return Thread.get(thread_id)

    @classmethod
    def update_view_count(cls, thread_id):
        Thread.update_view_count(thread_id)

class ArticleAPI(object):
    
    @classmethod
    def get_count(cls, thread_id):
        return Article.get_count(thread_id)

    @classmethod
    def get_article_list(cls, thread_id, is_last=False):
        return Article.get_article_list(thread_id, is_last)
    
    @classmethod
    def get(cls, article_id):
        return Article.get(article_id)
    
    @classmethod
    def post_article(cls, request, forum_id, thread_id, cleaned_data):
        body = cleaned_data['body']
        forum_id = int(forum_id)
        forum_status = cleaned_data['forum_status']
        status_obj = None
        if forum_status:
            status_obj = ForumStatusAPI.get(forum_status)
        
        if 'status_change_pass' in cleaned_data:
            user_name = cleaned_data['user_name']
            status_change_pass = cleaned_data['status_change_pass']
            thread = Thread.get(thread_id)
            thread.last_article_update_at = datetime.datetime.now()
            if status_change_pass and forum_status and thread.status_change_pass == status_change_pass:
                thread.forum_status_id = forum_status
                if status_obj and status_obj.is_thread_rock:
                    thread.is_rock = True
            thread.save()
    
            article = Article.objects.create(forum_id=forum_id, thread=thread, body=body, user_id=0, user_name=user_name)
            article.save()
        
        else:
            is_rock = cleaned_data['is_rock']
            
            thread = Thread.get(thread_id)
            if is_rock:
                thread.is_rock = is_rock
            if forum_status:
                thread.forum_status_id = forum_status
                if status_obj and status_obj.is_thread_rock:
                    thread.is_rock = True
            thread.last_article_update_at = datetime.datetime.now()
            thread.save()
    
            article = Article.objects.create(forum_id=forum_id, thread=thread, body=body, user_id=request.user.id)
            article.save()

    @classmethod
    def update_article(cls, request, article_id, cleaned_data):
        body = cleaned_data['body']
        edit_mean = cleaned_data['edit_mean']

        article = Article.get(article_id)

        if article.user_id != request.user.id:
            return

        article.body = body
        article.is_edit = True
        article.edit_mean = edit_mean
        article.edit_at = datetime.datetime.now()
        article.save()

    @classmethod
    def delete_article(cls, request, article_id, cleaned_data):
        delete_mean = cleaned_data['delete_mean']

        article = Article.get(article_id)

        if article.user_id != request.user.id and not request.user.is_staff:
            return

        article.is_delete = True
        article.delete_mean = delete_mean
        article.delete_user_id = request.user.id
        article.save()

    @classmethod
    def search(cls, request, cleaned_data):
        body = cleaned_data['body']
        choice_type = cleaned_data['choice_type']
        forum_id = cleaned_data['forum_id']

        forum_id = int(forum_id)
        choice_type = int(choice_type)
        body = body.replace(u'　', u' ')
        word_list = body.split()

        return Article.get_search_article_list(forum_id, choice_type, word_list)

    @classmethod
    def lastest(cls):
        return Article.get_lastest_article_list()

    @classmethod
    def update_good_count(cls, article_id, user):
        return Article.update_good_count(article_id, user)
        
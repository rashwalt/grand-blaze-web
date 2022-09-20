# -*- coding: utf-8 -*-

from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.tag
def pager(parser, token):
    try:
        args = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly 2 argument" % token.contents.split()[0]
    if args[1] == u'request':
        return PagerNode(args[2], args[3], args[4:])
    elif args[1] == u'pager':
        return PagerNode(args[1], args[2], args[3:])

class PagerNode(template.Node):

    VIEW_PAGE_NUM_RANGE = 2

    def __init__(self, pager, url_name, url_args):
        self.pager      = template.Variable(pager)
        self.url_name   = template.Variable(url_name)
        self.url_args   = [template.Variable(url_arg) for url_arg in url_args]

    def render(self, context):
        pager    = self.pager.resolve(context)
        url_name = self.url_name.resolve(context)
        # 基本的なURL引数を設定
        url_args = []
        for url_arg in self.url_args:
            url_args.append(url_arg.resolve(context))

        # 前と次へのリンクを生成
        context['pager'] = pager
        context['next_url'] = reverse(url_name, args=url_args + [pager['next_page']]) if pager['next_page'] else ''
        context['prev_url'] = reverse(url_name, args=url_args + [pager['previous_page']]) if pager['previous_page'] else ''

        # VIEW_PAGE_NUM_RANGE*2+1分のページリンクを表示する
        min_page = pager['current_page']-self.VIEW_PAGE_NUM_RANGE
        max_page = pager['current_page']+self.VIEW_PAGE_NUM_RANGE
        if min_page < 1:
            max_page += 1 - min_page
        if max_page > pager['last_page']:
            min_page -= max_page - pager['last_page']
        # バグ対策でmin_pageが1未満の場合、1にする
        if min_page < 1:
            min_page = 1

        # リンクページを生成する
        context['page_urls'] = [{'num': i, 'url': reverse(url_name, args=url_args + [i])}
            for i in range(min_page, pager['last_page']+1) if i <= max_page]

        # レンダリングして返す
        t = template.loader.get_template('parts/pager.html')
        html = t.render(context)

        return html
    

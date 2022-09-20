# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, InvalidPage

def get_pager_from_list(list, limit=5, page=1, navigation_len=10):
    """
    リストからページング生成
    """
    page = int(page)
    total = len(list)
    per_page = int(limit)
    last_page = int(total / limit)
    if total % limit > 0:
        last_page += 1
    first = per_page  * (page - 1) + 1
    last = first + per_page -1

    limit_page = int(navigation_len/2)
    min = page - limit_page
    max = page + limit_page

    if min <= 0:
        navigation_first_page = 1
    else:
        navigation_first_page = min

    if max > total:
        navigation_last_page = total
    else:
        navigation_last_page = max

    if last > total:
        last = total
    pager ={
        "total":total,
        "per_page":per_page,
        "first_page":1,
        "last_page":last_page,
        "current_page":page,
        "previous_page": 0,
        "next_page": 0,
        "first":first,
        "last":last,
        "prev_navigation_page":0,
        "next_navigation_page":0,
        "navigation_first_page":navigation_first_page,
        "navigation_last_page":navigation_last_page,
        "navigation":[]
        };
    if page > 1:
        pager["previous_page"] = page - 1
    if page < last_page:
        pager["next_page"] = page + 1

    if page>= limit_page:
        pager["prev_navigation_page"] = navigation_first_page - 1
    if page < total - limit_page:
        pager["next_navigation_page"] = navigation_last_page + 1

    for n in range(1,last_page + 1):
        if n >= min and n < max + 1:
            pager["navigation"].append(n)
    list = list[first-1:last]

    return pager, list
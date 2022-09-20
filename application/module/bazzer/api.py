# -*- coding: utf-8 -*-

import datetime

from module.bazzer.models import Bazzer

from module.character.api import CharacterAPI, CharacterHaveItemAPI
from module.master.item.models import Item

class BazzerAPI(object):
    
    @classmethod
    def search(cls, request, cleaned_data):
        user = request.user
        type = cleaned_data['type']
        level = cleaned_data['level']
        min_price = cleaned_data['min_price']
        max_price = cleaned_data['max_price']
        sort = cleaned_data['sort']
        is_mine = cleaned_data['is_mine']
        is_buy = cleaned_data['is_buy']

        type = int(type)
        if level:
            level = int(level)
        if min_price:
            min_price = int(min_price)
        if max_price:
            max_price = int(max_price)
        sort = int(sort)

        return Bazzer.get_search_article_list(user, type, level, min_price, max_price, sort, is_mine, is_buy)
    
    @classmethod
    def create(cls, request, cleaned_data):
        seller_having_no = cleaned_data['seller_having_no']
        price = cleaned_data['price']
        user = request.user
        
        having_no = int(seller_having_no)
        price = int(price)
        
        items = CharacterHaveItemAPI.get_filter_by_haved(user, having_no)
        if items:
            item = Item.get(items.item_v_id)
            
            # バザーに出せるアイテム？
            if item.it_bind or item.it_quest:
                return -1, u'バザー出品できませんでした。このアイテムはバインドアイテム、またはクエスト用のアイテムであるため、バザーに出品できません。'
            
            # 限界まで出品してないか？
            if items.it_box_count <= 0:
                return -1, u'バザー出品できませんでした。これ以上このアイテムを出品できるほど所持していません。'
        else:
            return -1, u'バザー出品できませんでした。選択されたアイテムの情報を取得できませんでした。'

        items.it_box_baz_count += 1
        items.it_box_count -= 1
        items.save()
        return Bazzer.create(user, item, having_no, price)
    
    @classmethod
    def get(cls, bazzer_id):
        return Bazzer.get(bazzer_id)
    
    @classmethod
    def buy(cls, request, bazzer_id):
        bazzer_id = int(bazzer_id)
        user = request.user

        is_buy = Bazzer.buy(user, bazzer_id)
        if is_buy:
            bazzer_data = cls.get(bazzer_id)
            character = CharacterAPI.get(user)
            character.have_money -= bazzer_data.price
            character.save()
        return is_buy
    
    @classmethod
    def cancel(cls, request, bazzer_id):
        bazzer_id = int(bazzer_id)
        user = request.user
        
        is_bazzer = Bazzer.cancel(user, bazzer_id)
        bazzer_data = cls.get(bazzer_id)

        items = CharacterHaveItemAPI.get_filter_by_haved(user, bazzer_data.seller_having_no)
        
        if items:
            items.it_box_baz_count -= 1
            items.it_box_count += 1
            items.save()
        return is_bazzer
    
    @classmethod
    def get_item_history_list(cls, item_id):
        return Bazzer.get_item_history_list(item_id)
        
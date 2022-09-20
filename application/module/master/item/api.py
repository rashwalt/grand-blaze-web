# -*- coding: utf-8 -*-

from module.master.item.models import Item, ItemType

class ItemAPI(object):
    
    @classmethod
    def get_by_category(cls, category_id):
        return Item.get_chices_list(category_id)
    

class ItemTypeAPI(object):
    
    @classmethod
    def get(cls, type_id):
        return ItemType.get(type_id)

    @classmethod
    def get_choice_list(cls):
        item_type = ItemType.get_choice_list()
        item_type.insert(0, (0, u'すべて'))
        return item_type



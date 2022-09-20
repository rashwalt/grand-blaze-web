# -*- coding: utf-8 -*-

from django.template.loader import render_to_string

from module.character.models import Character
from module.regist.continue_complete.models import ContinueComplete
from module.regist.continue_trade.models import ContinueShopping, ContinueTrade
from module.regist.constant import RegistConstant

class ContinueTradeAPI(object):
    
    @classmethod
    def get(cls, user_id):
        return ContinueTrade.get_filter_by_user(user_id)
    
    @classmethod
    def get_query_trade_item(cls, user_id):
        return ContinueTrade.objects.filter(user=user_id, trade_item_no__gt=0)
    
    @classmethod
    def get_query_trade_money(cls, user_id):
        return ContinueTrade.objects.filter(user=user_id, trade_item_no=0)
    
    @classmethod
    def get_query_sell(cls, user_id):
        return ContinueShopping.objects.filter(user=user_id, shop_act=RegistConstant.SHOP_ACT_SELL)
    
    @classmethod
    def get_query_buy(cls, user_id):
        return ContinueShopping.objects.filter(user=user_id, shop_act=RegistConstant.SHOP_ACT_BUY)
    
    @classmethod
    def update_continue_trade(cls, request, continue_trade_items, continue_trade_moneys, continue_sell_shoppings, continue_buy_shoppings):
        user = request.user
        
        # 送信者情報
        ip_address = request.META.get('REMOTE_ADDR','')
        host = request.META.get('REMOTE_HOST', '')
        agent = request.META.get('HTTP_USER_AGENT','')
        
        continue_shop_del_list = ContinueShopping.get_filter_by_user(user.id)
        for del_data in continue_shop_del_list:
            del_data.delete()
            
        continue_trade_del_list = ContinueTrade.get_filter_by_user(user.id)
        for del_data in continue_trade_del_list:
            del_data.delete()
        
        # Continue Trade And Shop multi save
        number = 1
        for temp_data in continue_sell_shoppings:
            ContinueShopping.objects.create(user=user, shop_act=RegistConstant.SHOP_ACT_SELL, shopping_no=number, item_no=temp_data.item_no, item_count=temp_data.item_count, ip_address=ip_address, host_address=host, user_agent=agent)
            number = number + 1
            
        number = 1
        for temp_data in continue_buy_shoppings:
            ContinueShopping.objects.create(user=user, shop_act=RegistConstant.SHOP_ACT_BUY, shopping_no=number, item_no=temp_data.item_no, item_count=temp_data.item_count, ip_address=ip_address, host_address=host, user_agent=agent)
            number = number + 1
            
        number = 1
        for temp_data in continue_trade_items:
            if not temp_data.trade_item_no:
                temp_data.trade_number = 0
            ContinueTrade.objects.create(user=user, trade_no=number, trade_entry=temp_data.trade_entry, trade_item_no=temp_data.trade_item_no, trade_number=temp_data.trade_number, trade_message=temp_data.trade_message, trade_speed=temp_data.trade_speed, ip_address=ip_address, host_address=host, user_agent=agent)
            number = number + 1
            
        number = 1
        for temp_data in continue_trade_moneys:
            ContinueTrade.objects.create(user=user, trade_no=number, trade_entry=temp_data.trade_entry, trade_item_no=0, trade_number=temp_data.trade_number, trade_message=temp_data.trade_message, trade_speed=temp_data.trade_speed, ip_address=ip_address, host_address=host, user_agent=agent)
            number = number + 1
        
        # Continue Complete
        ContinueComplete.completed(user, 'trade', ip_address, host, agent)
    
    @classmethod
    def get_mail(cls, user):
        character = Character.get(user.id)
        
        continue_sell_shoppings = cls.get_query_sell(user.id)
        continue_buy_shoppings = cls.get_query_buy(user.id)
        continue_trade_items = cls.get_query_trade_item(user.id)
        continue_trade_moneys = cls.get_query_trade_money(user.id)
        
        ctxt = {
                'user_id': user.id,
                'character_name': character.character_name,
                'sell_datas': continue_sell_shoppings,
                'buy_datas': continue_buy_shoppings,
                'item_datas': continue_trade_items,
                'money_datas': continue_trade_moneys,
                }
        
        return render_to_string('regist/continue_trade/mail.html', ctxt)
        
class ContinueShoppingAPI(object):
    
    @classmethod
    def get(cls, user_id):
        return ContinueShopping.get_filter_by_user(user_id)
    
    @classmethod
    def get_query_sell(cls, user_id):
        return ContinueShopping.objects.filter(user=user_id, shop_act=RegistConstant.SHOP_ACT_SELL)
    
    @classmethod
    def get_query_buy(cls, user_id):
        return ContinueShopping.objects.filter(user=user_id, shop_act=RegistConstant.SHOP_ACT_BUY)
        
        
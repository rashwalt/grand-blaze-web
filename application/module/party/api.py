# -*- coding: utf-8 -*-

from module.party.models import Party, PartyBelong

class PartyAPI(object):

    @classmethod
    def get(cls, party_id):
        return Party.get(party_id)
    
    @classmethod
    def get_party_member(cls, user):
        
        party_belong = PartyBelong.get(user.id)
        
        if party_belong:
            return PartyBelong.get_filter_by_party_id(party_belong.party_id)
        else:
            return []
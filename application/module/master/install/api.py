# -*- coding: utf-8 -*-

from module.master.install.models import Install, InstallSkill

class InstallAPI(object):
    
    @classmethod
    def get(cls, install_id):
        return Install.get(install_id)
    
    @classmethod
    def get_choices_list(cls):
        return Install.get_chices_list()
    
    @classmethod
    def get_under_install(cls, install_id, level):
        return InstallSkill.get_list_by_under(install_id, level)
    
    @classmethod
    def get_install_skill(cls, install_id):
        return InstallSkill.get_list(install_id)
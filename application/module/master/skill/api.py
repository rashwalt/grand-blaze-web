# -*- coding: utf-8 -*-

from module.master.skill.models import Skill, SkillGet, SkillGetList, SkillCategory

from module.character.models import CharacterHavingSkill

class SkillAPI(object):
    
    @classmethod
    def get_list_by_type(cls, skill_type_id):
        return Skill.get_list_by_type(skill_type_id)

class SkillGetListAPI(object):
    
    @classmethod
    def get_selection_list(cls, user):
        select_skill_ids = SkillGet.get_skill_id_list(user)
        
        skill_list = SkillGetList.get_sorted_level_list()
        
        haved_skill_ids = CharacterHavingSkill.get_skill_id_list(user)
        
        new_skill_list = []
        
        for skill_data in skill_list:
            new_skill_data = {'tm_level': skill_data.tm_level, 'skill_name': skill_data.skill.name, 'skill_id': skill_data.skill_id, 'condition_text': skill_data.condition_text, 'sk_comment': skill_data.skill.sk_comment, } 
            new_skill_data['is_having'] = 0

            if skill_data.skill_id in haved_skill_ids:
                new_skill_data['is_having'] = 1
                new_skill_list.append(new_skill_data)
                continue
            
            if skill_data.skill_id in select_skill_ids:
                new_skill_data['is_having'] = 2
                
            new_skill_list.append(new_skill_data)
        
        return new_skill_list
    
    @classmethod
    def get_private_list(cls):
        
        return SkillGetList.get_sorted_level_list()

class SkillCategoryAPI(object):
    
    @classmethod
    def get(cls, category_id):
        return SkillCategory.get(category_id)
# -*- coding: utf-8 -*-

import re
import random

from django.conf import settings
from django.utils import html

from module.character.api import CharacterAPI

class PreviewUtil(object):
	_entry_no = 0
	_mine_name = '';
	
	SERIF_COMMAND_PATTERN = re.compile(r'(/[a-z]+ )')
	SUB_COMMAND_PATTERM = re.compile(r'([a-z0-9]+ )')
	
	RANGE_REPLACE = {
            'b': [ 'strong', '' ],
            'i': [ 'em', '' ],
            'u': [ 'u', '' ],
            's': [ 'strike', '' ], 
            'sh': [ 'span', 'class="serif_shout"' ],
            'lo': [ 'span', 'class="serif_low"' ],
            'gray': [ 'span', 'class="serif_gray"' ],
            'silver': [ 'span', 'class="serif_silver"' ],
            'maroon': [ 'span', 'class="serif_maroon"' ],
            'red': [ 'span', 'class="serif_red"' ],
            'olive': [ 'span', 'class="serif_olive"' ],
            'yellow': [ 'span', 'class="serif_yellow"' ],
            'green': [ 'span', 'class="serif_green"' ],
            'lime': [ 'span', 'class="serif_lime"' ],
            'teal': [ 'span', 'class="serif_teal"' ],
            'aqua': [ 'span', 'class="serif_aqua"' ],
            'navy': [ 'span', 'class="serif_navy"' ],
            'blue': [ 'span', 'class="serif_blue"' ],
            'purple': [ 'span', 'class="serif_purple"' ],
            'fuchsia': [ 'span', 'class="serif_fuchsia"' ],
    }
	
	def __init__(self, user):
		self._entry_no = user.id
		
		character = CharacterAPI.get(user)
		
		self._mine_name = character.nick_name
	
	def convert(self, conv_word, is_list=False):
		"""
		変換
		"""
		conv_word = conv_word.replace(u'<br>{nl}', u'{nl}').replace(u'{nl}<br>', u'{nl}').replace(u'<br />{nl}', u'{nl}').replace(u'{nl}<br />', u'{nl}')
		
		# <nl>による分割
		word_list = conv_word.split(u'{nl}')
		serif_list = []
		
		for serif_body in word_list:
			serif_command = u'/say'
			is_serif_command = False
			serif_body = serif_body.strip()
			
			serif_body = html.escape(serif_body)
			serif_body = serif_body.replace(u'\n', '<br />')
			
			match_obj = self.SERIF_COMMAND_PATTERN.match(serif_body)
			
			if match_obj:
				print match_obj.groups()
				match_str = match_obj.group(1)
				serif_command = match_str.strip()
				serif_body = serif_body.replace(match_str, '')
				is_serif_command = True
			
			icon_tag = ''
			icon_add_class = ''
			icon_size = 0
			
			if is_list:
				if is_serif_command:
					serif_body = '%s %s' % (serif_command, serif_body)
				serif_body = self._convert_message(serif_body)
				serif_list.append(u'<p>%s</p>' % (serif_body))
			elif serif_command in [u'/say', u'/s']:
				# セイ
				serif_body, icon_tag, icon_size = self._sub_command(serif_body, icon_tag)
				serif_body = self._convert_message(serif_body)
				icon_add_class = self._icon_add_class(icon_tag, icon_size)
				serif_list.append(u'<dl class="private_serif%s"><dt>%s<span class="friend">%s</span></dt><dd>「%s」</dd></dl>' % (icon_add_class, icon_tag, self._mine_name, serif_body))
			elif serif_command in [u'/shout', u'/sh']:
				# シャウト
				serif_body, icon_tag, icon_size = self._sub_command(serif_body, icon_tag)
				serif_body = self._convert_message(serif_body)
				icon_add_class = self._icon_add_class(icon_tag, icon_size)
				serif_list.append(u'<dl class="private_serif%s"><dt>%s<span class="friend">%s</span></dt><dd>「<span class="serif_shout">%s</span>」</dd></dl>' % (icon_add_class, icon_tag, self._mine_name, serif_body))
			elif serif_command in [u'/low', u'/lo']:
				# ロウ
				serif_body, icon_tag, icon_size = self._sub_command(serif_body, icon_tag)
				serif_body = self._convert_message(serif_body)
				icon_add_class = self._icon_add_class(icon_tag, icon_size)
				serif_list.append(u'<dl class="private_serif%s"><dt>%s<span class="friend">%s</span></dt><dd>「<span class="serif_low">%s</span>」</dd></dl>' % (icon_add_class, icon_tag, self._mine_name, serif_body))
			elif serif_command in [u'/emotion', u'/em']:
				# エモーション
				serif_body, icon_tag, icon_size = self._sub_command(serif_body, icon_tag)
				serif_body = self._convert_message(serif_body)
				icon_add_class = self._icon_add_class(icon_tag, icon_size)
				serif_list.append(u'<p class="private_serif%s serif_emotion">%s%s</p>' % (icon_add_class, icon_tag, serif_body))
			elif serif_command in [u'/other', u'/o']:
				# アザー
				if not ' ' in serif_body:
					continue
				other_index = serif_body.index(' ')
				serif_other = serif_body[:other_index]
				serif_body = serif_body[other_index:].strip()
				if not serif_body:
					continue
				
				serif_body, icon_tag, icon_size = self._sub_command(serif_body, icon_tag)
				serif_body = self._convert_message(serif_body)
				icon_add_class = self._icon_add_class(icon_tag, icon_size)
				serif_list.append(u'<dl class="private_serif%s"><dt>%s<span class="friend serif_other">%s</span></dt><dd>「%s」</dd></dl>' % (icon_add_class, icon_tag, serif_other, serif_body))
			elif serif_command in [u'/othershout', u'/os']:
				# アザーシャウト
				if not ' ' in serif_body:
					continue
				other_index = serif_body.index(' ')
				serif_other = serif_body[:other_index]
				serif_body = serif_body[other_index:].strip()
				if not serif_body:
					continue
				
				serif_body, icon_tag, icon_size = self._sub_command(serif_body, icon_tag)
				serif_body = self._convert_message(serif_body)
				icon_add_class = self._icon_add_class(icon_tag, icon_size)
				serif_list.append(u'<dl class="private_serif%s"><dt>%s<span class="friend serif_other">%s</span></dt><dd>「<span class="serif_shout">%s</span>」</dd></dl>' % (icon_add_class, icon_tag, serif_other, serif_body))
			elif serif_command in [u'/otherlow', u'/ol']:
				# アザーロウ
				if not ' ' in serif_body:
					continue
				other_index = serif_body.index(' ')
				serif_other = serif_body[:other_index]
				serif_body = serif_body[other_index:].strip()
				if not serif_body:
					continue
				
				serif_body, icon_tag, icon_size = self._sub_command(serif_body, icon_tag)
				serif_body = self._convert_message(serif_body)
				icon_add_class = self._icon_add_class(icon_tag, icon_size)
				serif_list.append(u'<dl class="private_serif%s"><dt>%s<span class="friend serif_other">%s</span></dt><dd>「<span class="serif_low">%s</span>」</dd></dl>' % (icon_add_class, icon_tag, serif_other, serif_body))
			
		return u'\n'.join(serif_list)
	
	def _sub_command(self, serif_body, icon_tag):
		"""
		サブコマンド
		"""
		match_obj = self.SUB_COMMAND_PATTERM.match(serif_body)
		
		sub_serif_command = ''
		
		if match_obj and len(match_obj.groups()) > 0:
			match_str = match_obj.group(1)
			sub_serif_command = match_str.strip()
			serif_body = serif_body.replace(match_str, '')
		
		if not sub_serif_command:
			return serif_body, icon_tag, 0
		
		icon_no = 1
		icon_string = sub_serif_command
		icon_string = icon_string.replace(u'sicon', u'').replace(u'licon', u'').replace(u'icon', u'')
		if icon_string.isdigit():
			sub_serif_command = sub_serif_command.replace(icon_string, '')
			icon_no = int(icon_string)
		
		sub_serif_command = sub_serif_command.strip()
		icon_size = 0
		
		if sub_serif_command == u'icon':
			icon_tag = self._get_icon_url(icon_no, 'M')
			icon_size = 2
		elif sub_serif_command == u'sicon':
			icon_tag = self._get_icon_url(icon_no, 'S')
			icon_size = 1
		elif sub_serif_command == u'licon':
			icon_tag = self._get_icon_url(icon_no, 'L')
			icon_size = 3
		else:
			serif_body = u'%s %s' % (sub_serif_command, serif_body)
		
		return serif_body, icon_tag, icon_size
	
	def _icon_add_class(self, icon_tag, icon_size):
		if icon_tag:
			if icon_size == 1:
				return u' sics'
			elif icon_size == 2:
				return u' sic'
			elif icon_size == 3:
				return u' sicl'
		
		return ''
	
	def _convert_message(self, serif_body):
		#{t}  	行動の対象（攻撃目標となっている敵など）の名前（愛称）を指す代名詞です。複数が対象の場合は展開されません。
		serif_body = serif_body.replace(u'{t}', u'サンプルターゲット')
		#{hp} 	自分のHPを 現在値/最大値 で表示します。
		serif_body = serif_body.replace(u'{hp}', u'150/200')
		#{hpp} 	自分のHPを％で表示します。
		serif_body = serif_body.replace(u'{hpp}', u'75%')
		#{hppr} 	自分のHPの減少量を％で表示します。
		serif_body = serif_body.replace(u'{hppr}', u'25%')
		#{mp} 	自分のMPを 現在値/最大値 で表示します。
		serif_body = serif_body.replace(u'{mp}', u'75/100')
		#{mpp} 	自分のMPを％で表示します。
		serif_body = serif_body.replace(u'{mpp}', u'75%')
		#{mppr} 	自分のMPの減少量を％で表示します。
		serif_body = serif_body.replace(u'{mppr}', u'25%')
		#{tp} 	自分のTPを 現在値/最大値 で表示します。
		serif_body = serif_body.replace(u'{tp}', u'75/100')
		#{tpp} 	自分のTPを％で表示します。
		serif_body = serif_body.replace(u'{tpp}', u'75%')
		#{tppr} 	自分のTPの減少量を％で表示します。
		serif_body = serif_body.replace(u'{tppr}', u'25%')
		#{me} 	自分の愛称を指す代名詞です。
		serif_body = serif_body.replace(u'{me}', self._mine_name)
		#{pos} 	現在のエリア名称を指す代名詞です。
		serif_body = serif_body.replace(u'{pos}', u'サンプルクエスト')
		#{br} 	指定された場所で改行します。
		serif_body = serif_body.replace(u'{br}', u'<br />')
		#{random} 	1～999の数字をランダムで表示します。
		serif_body = serif_body.replace(u'{random}', unicode(str(random.randint(1,999))))
		#{dc} 	トドメを刺した数
		serif_body = serif_body.replace(u'{dc}', u'42')
		#{dcj} 	トドメを刺した数(漢数字版)
		serif_body = serif_body.replace(u'{dcj}', u'四十二')
		#{main} 	現在装備しているメインの装備名称
		serif_body = serif_body.replace(u'{main}', u'サンプルメインウェポン')
		#{sub} 	現在装備しているメインの装備名称
		serif_body = serif_body.replace(u'{sub}', u'サンプルサブウェポン')
		#{head} 	現在装備しているメインの装備名称
		serif_body = serif_body.replace(u'{head}', u'サンプル頭部防具')
		#{body} 	現在装備しているメインの装備名称
		serif_body = serif_body.replace(u'{body}', u'サンプル身体防具')
		#{acce} 	現在装備しているメインの装備名称
		serif_body = serif_body.replace(u'{acce}', u'サンプルアクセサリー')
		#{arts} 	発動したアーツ名称
		serif_body = serif_body.replace(u'{arts}', u'サンプルアーツ')
		
		for key, value in self.RANGE_REPLACE.items():
			tag, attr = value
			if attr:
				attr = u' %s' % attr
			serif_body = serif_body.replace(u'{%s}' % key, u'<%s%s>' % (tag, attr))
			serif_body = serif_body.replace(u'{/%s}' % key, u'</%s>' % tag)
		
		
		return serif_body
	
	def _get_icon_url(self, icon_no, icon_size):
		size = 48
		
		if icon_size == 'L':
			size = 64
		elif icon_size == 'S':
			size = 32
		
		return u'<img src="%s/images/common/icon_sample.gif" alt="(C)著作者:著作者名" width="%s" height="%s" class="ch_icon" />' % (settings.MEDIA_URL, size, size)


# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Item'
        db.create_table('item_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('it_physics', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_sorcery', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_physics_parry', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_sorcery_parry', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_critical', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_metal', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_charge', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_range', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_sub_category', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_attack_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('it_fire', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_freeze', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_air', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_earth', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_water', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_thunder', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_holy', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_dark', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_slash', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_pierce', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_strike', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_break', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_ok_sex', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_ok_race', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_both_hand', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('it_use_item', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_equip_install', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('it_equip_parts', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('it_rare', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('it_bind', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('it_quest', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('it_shop', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_equip_level', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_target_area', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('it_price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=13, decimal_places=1)),
            ('it_seller', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=13, decimal_places=1)),
            ('it_stack', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('item', ['Item'])

        # Adding model 'ItemType'
        db.create_table('item_itemtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('skill_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('categ_div', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('database_view', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('it_stack', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('item', ['ItemType'])


    def backwards(self, orm):
        
        # Deleting model 'Item'
        db.delete_table('item_item')

        # Deleting model 'ItemType'
        db.delete_table('item_itemtype')


    models = {
        'item.item': {
            'Meta': {'object_name': 'Item'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'it_air': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_attack_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_bind': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'it_both_hand': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'it_break': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_charge': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'it_critical': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_dark': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_earth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_equip_install': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'it_equip_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_equip_parts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'it_fire': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_freeze': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_holy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_metal': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_ok_race': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_ok_sex': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_physics': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_physics_parry': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_pierce': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '13', 'decimal_places': '1'}),
            'it_quest': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'it_range': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_rare': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'it_seller': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '13', 'decimal_places': '1'}),
            'it_shop': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_slash': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_sorcery': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_sorcery_parry': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_stack': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_strike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_sub_category': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_target_area': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_thunder': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_use_item': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_water': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'item.itemtype': {
            'Meta': {'object_name': 'ItemType'},
            'categ_div': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'database_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'it_stack': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'skill_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['item']

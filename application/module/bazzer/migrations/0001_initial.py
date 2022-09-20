# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bazzer'
        db.create_table('bazzer_bazzer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['item.Item'])),
            ('seller', self.gf('django.db.models.fields.related.ForeignKey')(related_name='seller_users', to=orm['auth.User'])),
            ('price', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('seller_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 9, 17, 0, 0))),
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('buyer', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='buyer_users', null=True, blank=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('bazzer', ['Bazzer'])


    def backwards(self, orm):
        # Deleting model 'Bazzer'
        db.delete_table('bazzer_bazzer')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'bazzer.bazzer': {
            'Meta': {'object_name': 'Bazzer'},
            'buyer': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'buyer_users'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['item.Item']"}),
            'price': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'seller': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'seller_users'", 'to': "orm['auth.User']"}),
            'seller_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 17, 0, 0)'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        }
    }

    complete_apps = ['bazzer']
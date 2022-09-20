# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Quest.bc_level'
        db.add_column('quest_quest', 'bc_level',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Quest.bc_level'
        db.delete_column('quest_quest', 'bc_level')


    models = {
        'quest.fieldtype': {
            'Meta': {'object_name': 'FieldType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'quest.mark': {
            'Meta': {'object_name': 'Mark'},
            'field_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hide_mark': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quest.Quest']"})
        },
        'quest.markweather': {
            'Meta': {'object_name': 'MarkWeather'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mark': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quest.Mark']"}),
            'weather': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quest.Weather']"})
        },
        'quest.quest': {
            'Meta': {'object_name': 'Quest'},
            'bc_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'class_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'comp_quest_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hide_fg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'install_class_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'keyitem_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'offer_quest_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pick_level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'quest_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sp_level': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'quest.weather': {
            'Meta': {'object_name': 'Weather'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['quest']
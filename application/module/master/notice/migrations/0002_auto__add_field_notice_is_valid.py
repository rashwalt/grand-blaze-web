# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Notice.is_valid'
        db.add_column('notice_notice', 'is_valid',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Notice.is_valid'
        db.delete_column('notice_notice', 'is_valid')


    models = {
        'notice.notice': {
            'Meta': {'object_name': 'Notice'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'limit_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'view_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 8, 30, 0, 0)'})
        }
    }

    complete_apps = ['notice']
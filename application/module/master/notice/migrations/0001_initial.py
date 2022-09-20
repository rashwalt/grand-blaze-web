# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Notice'
        db.create_table('notice_notice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=50)),
            ('view_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('limit_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('notice', ['Notice'])


    def backwards(self, orm):
        
        # Deleting model 'Notice'
        db.delete_table('notice_notice')


    models = {
        'notice.notice': {
            'Meta': {'object_name': 'Notice'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'view_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['notice']

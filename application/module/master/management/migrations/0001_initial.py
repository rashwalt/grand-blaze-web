# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Management'
        db.create_table('management_management', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_regist_stop', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('management', ['Management'])


    def backwards(self, orm):
        
        # Deleting model 'Management'
        db.delete_table('management_management')


    models = {
        'management.management': {
            'Meta': {'object_name': 'Management'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_regist_stop': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['management']

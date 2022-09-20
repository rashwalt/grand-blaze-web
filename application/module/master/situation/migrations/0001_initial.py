# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Situation'
        db.create_table('situation_situation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('it_comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('situation', ['Situation'])


    def backwards(self, orm):
        
        # Deleting model 'Situation'
        db.delete_table('situation_situation')


    models = {
        'situation.situation': {
            'Meta': {'object_name': 'Situation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'it_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['situation']

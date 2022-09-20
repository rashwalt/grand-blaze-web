# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BattleAction'
        db.create_table('battleaction_battleaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comment', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('battleaction', ['BattleAction'])

        # Adding model 'BattleTarget'
        db.create_table('battleaction_battletarget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comment', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('view_no', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('target_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('target_no', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('battleaction', ['BattleTarget'])


    def backwards(self, orm):
        
        # Deleting model 'BattleAction'
        db.delete_table('battleaction_battleaction')

        # Deleting model 'BattleTarget'
        db.delete_table('battleaction_battletarget')


    models = {
        'battleaction.battleaction': {
            'Meta': {'object_name': 'BattleAction'},
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'battleaction.battletarget': {
            'Meta': {'object_name': 'BattleTarget'},
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'target_no': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'target_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'view_no': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['battleaction']

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Quest'
        db.create_table('quest_quest', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('quest_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pick_level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('keyitem_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('offer_quest_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('comp_quest_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sp_level', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('install_class_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('class_level', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hide_fg', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('quest', ['Quest'])

        # Adding model 'Mark'
        db.create_table('quest_mark', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quest.Quest'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('field_type', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hide_mark', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('quest', ['Mark'])


    def backwards(self, orm):
        
        # Deleting model 'Quest'
        db.delete_table('quest_quest')

        # Deleting model 'Mark'
        db.delete_table('quest_mark')


    models = {
        'quest.mark': {
            'Meta': {'object_name': 'Mark'},
            'field_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hide_mark': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quest.Quest']"})
        },
        'quest.quest': {
            'Meta': {'object_name': 'Quest'},
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
        }
    }

    complete_apps = ['quest']

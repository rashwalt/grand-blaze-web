# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Race'
        db.create_table('race_race', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('up_hp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('up_mp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('up_str', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('up_dex', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('up_agi', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('up_mag', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('up_vit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('up_unq', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('race', ['Race'])


    def backwards(self, orm):
        
        # Deleting model 'Race'
        db.delete_table('race_race')


    models = {
        'race.race': {
            'Meta': {'object_name': 'Race'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'up_agi': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'up_dex': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'up_hp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'up_mag': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'up_mp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'up_str': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'up_unq': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'up_vit': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['race']

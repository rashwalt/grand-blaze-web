# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Install'
        db.create_table('install_install', (
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
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('install', ['Install'])


    def backwards(self, orm):
        
        # Deleting model 'Install'
        db.delete_table('install_install')


    models = {
        'install.install': {
            'Meta': {'object_name': 'Install'},
            'comment': ('django.db.models.fields.TextField', [], {}),
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

    complete_apps = ['install']

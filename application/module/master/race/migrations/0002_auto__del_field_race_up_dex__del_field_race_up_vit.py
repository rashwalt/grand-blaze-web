# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Race.up_dex'
        db.delete_column('race_race', 'up_dex')

        # Deleting field 'Race.up_vit'
        db.delete_column('race_race', 'up_vit')


    def backwards(self, orm):
        # Adding field 'Race.up_dex'
        db.add_column('race_race', 'up_dex',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Race.up_vit'
        db.add_column('race_race', 'up_vit',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    models = {
        'race.race': {
            'Meta': {'object_name': 'Race'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'up_agi': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'up_hp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'up_mag': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'up_mp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'up_str': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'up_unq': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['race']
# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'InstallSkill'
        db.create_table('install_installskill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('install', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['install.Install'])),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['skill.Skill'])),
            ('only_mode', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('install', ['InstallSkill'])

        # Adding unique constraint on 'InstallSkill', fields ['install', 'level', 'skill']
        db.create_unique('install_installskill', ['install_id', 'level', 'skill_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'InstallSkill', fields ['install', 'level', 'skill']
        db.delete_unique('install_installskill', ['install_id', 'level', 'skill_id'])

        # Deleting model 'InstallSkill'
        db.delete_table('install_installskill')


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
        },
        'install.installskill': {
            'Meta': {'unique_together': "(('install', 'level', 'skill'),)", 'object_name': 'InstallSkill'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'install': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['install.Install']"}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'only_mode': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skill.Skill']"})
        },
        'skill.skill': {
            'Meta': {'object_name': 'Skill'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sk_air': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_antiair': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_arts_category': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_atype': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_break': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_charge': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sk_critical': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_critical_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_damage_rate': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'sk_damage_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_dark': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_dhate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_earth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_effect': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sk_fire': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_freeze': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_hate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_hit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_holy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_mp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_pierce': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_plus_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_power': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '4'}),
            'sk_range': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_round': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_slash': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_sp_bash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_sp_conv': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_sp_fire': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_sp_hard': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_sp_pike': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_sp_scream': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_sp_slash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_sp_swing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sk_strike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_target_area': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_target_party': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_target_restrict': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_thunder': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_tp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_use_limit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_vhate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sk_water': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['install']

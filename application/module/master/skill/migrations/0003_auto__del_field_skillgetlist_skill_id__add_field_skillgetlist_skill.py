# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'SkillGetList.skill_id'
        db.delete_column('skill_skillgetlist', 'skill_id')

        # Adding field 'SkillGetList.skill'
        db.add_column('skill_skillgetlist', 'skill', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['skill.Skill']), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'SkillGetList.skill_id'
        db.add_column('skill_skillgetlist', 'skill_id', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Deleting field 'SkillGetList.skill'
        db.delete_column('skill_skillgetlist', 'skill_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 9, 1, 25, 24, 795000)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 9, 1, 25, 24, 795000)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
        },
        'skill.skillcategory': {
            'Meta': {'object_name': 'SkillCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'skill.skillget': {
            'Meta': {'object_name': 'SkillGet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'skill.skillgetlist': {
            'Meta': {'object_name': 'SkillGetList'},
            'condition_text': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['skill.Skill']"}),
            'tm_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tm_race': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['skill']

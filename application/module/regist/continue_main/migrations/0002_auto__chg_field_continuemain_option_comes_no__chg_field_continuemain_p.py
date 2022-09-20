# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'ContinueMain.option_comes_no'
        db.alter_column('continue_main_continuemain', 'option_comes_no', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ContinueMain.pcm_add_3'
        db.alter_column('continue_main_continuemain', 'pcm_add_3', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ContinueMain.pcm_add_4'
        db.alter_column('continue_main_continuemain', 'pcm_add_4', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ContinueMain.pcm_add_5'
        db.alter_column('continue_main_continuemain', 'pcm_add_5', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ContinueMain.use_item_3'
        db.alter_column('continue_main_continuemain', 'use_item_3', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ContinueMain.pcm_add_2'
        db.alter_column('continue_main_continuemain', 'pcm_add_2', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ContinueMain.use_item_1'
        db.alter_column('continue_main_continuemain', 'use_item_1', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ContinueMain.use_item_2'
        db.alter_column('continue_main_continuemain', 'use_item_2', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ContinueMain.pcm_add_1'
        db.alter_column('continue_main_continuemain', 'pcm_add_1', self.gf('django.db.models.fields.IntegerField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'ContinueMain.option_comes_no'
        db.alter_column('continue_main_continuemain', 'option_comes_no', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ContinueMain.pcm_add_3'
        db.alter_column('continue_main_continuemain', 'pcm_add_3', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ContinueMain.pcm_add_4'
        db.alter_column('continue_main_continuemain', 'pcm_add_4', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ContinueMain.pcm_add_5'
        db.alter_column('continue_main_continuemain', 'pcm_add_5', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ContinueMain.use_item_3'
        db.alter_column('continue_main_continuemain', 'use_item_3', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ContinueMain.pcm_add_2'
        db.alter_column('continue_main_continuemain', 'pcm_add_2', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ContinueMain.use_item_1'
        db.alter_column('continue_main_continuemain', 'use_item_1', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ContinueMain.use_item_2'
        db.alter_column('continue_main_continuemain', 'use_item_2', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ContinueMain.pcm_add_1'
        db.alter_column('continue_main_continuemain', 'pcm_add_1', self.gf('django.db.models.fields.IntegerField')())


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 21, 14, 27, 38, 305816)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 21, 14, 27, 38, 305700)'}),
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
        'continue_main.continuemain': {
            'Meta': {'object_name': 'ContinueMain'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'getting_private_skill': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'host_address': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'mark_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'option_comes_no': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'party_hope': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'party_name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'party_secession': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pcm_add_1': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pcm_add_2': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pcm_add_3': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pcm_add_4': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pcm_add_5': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'quest_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'use_item_1': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'use_item_2': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'use_item_3': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'primary_key': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'})
        }
    }

    complete_apps = ['continue_main']

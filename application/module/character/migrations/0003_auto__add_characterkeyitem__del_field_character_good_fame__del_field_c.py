# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CharacterKeyItem'
        db.create_table('character_characterkeyitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('keyitem_id', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('character', ['CharacterKeyItem'])

        # Deleting field 'Character.good_fame'
        db.delete_column('character_character', 'good_fame')

        # Deleting field 'Character.tarent_no'
        db.delete_column('character_character', 'tarent_no')

        # Deleting field 'Character.bad_fame'
        db.delete_column('character_character', 'bad_fame')


    def backwards(self, orm):
        
        # Deleting model 'CharacterKeyItem'
        db.delete_table('character_characterkeyitem')

        # Adding field 'Character.good_fame'
        db.add_column('character_character', 'good_fame', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Character.tarent_no'
        db.add_column('character_character', 'tarent_no', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Character.bad_fame'
        db.add_column('character_character', 'bad_fame', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 21, 20, 13, 33, 524000)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 21, 20, 13, 33, 524000)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'character.character': {
            'Meta': {'object_name': 'Character'},
            'account_status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'blaze_chip': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'character_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'continue_bonus': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'continue_cnt': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'familiar_name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'guardian_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'have_money': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'image_copyright': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            'image_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'image_link_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'image_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 21, 20, 13, 33, 459000)'}),
            'max_bazzeritem': ('django.db.models.fields.IntegerField', [], {'default': '7'}),
            'max_item': ('django.db.models.fields.IntegerField', [], {'default': '50'}),
            'nation_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_gamer': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'new_play': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nick_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '80'}),
            'profile': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'race_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'sex': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'unique_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '36'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'primary_key': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'character.characterkeyitem': {
            'Meta': {'object_name': 'CharacterKeyItem'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyitem_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['character']

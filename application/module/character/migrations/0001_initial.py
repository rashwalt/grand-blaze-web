# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Character'
        db.create_table('character_character', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='character_user', primary_key=True, to=orm['auth.User'])),
            ('continue_cnt', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('continue_bonus', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('account_status', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('new_play', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('new_gamer', self.gf('django.db.models.fields.IntegerField')()),
            ('character_name', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image_width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('image_height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('image_link_url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image_copyright', self.gf('django.db.models.fields.CharField')(max_length=180, blank=True)),
            ('nick_name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('tarent_no', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('race_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('guardian_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('nation_id', self.gf('django.db.models.fields.IntegerField')()),
            ('have_money', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('blaze_chip', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('bad_fame', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('good_fame', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sex', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('max_item', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('max_bazzeritem', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('profile', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('unique_name', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('familiar_name', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
        ))
        db.send_create_signal('character', ['Character'])


    def backwards(self, orm):
        
        # Deleting model 'Character'
        db.delete_table('character_character')


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 13, 1, 35, 43, 394000)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 13, 1, 35, 43, 394000)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'character.character': {
            'Meta': {'object_name': 'Character'},
            'account_status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bad_fame': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'blaze_chip': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'character_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'continue_bonus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'continue_cnt': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'familiar_name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'good_fame': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'guardian_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'have_money': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'image_copyright': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            'image_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'image_link_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'image_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'max_bazzeritem': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'max_item': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nation_id': ('django.db.models.fields.IntegerField', [], {}),
            'new_gamer': ('django.db.models.fields.IntegerField', [], {}),
            'new_play': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nick_name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'profile': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'race_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'sex': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'tarent_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unique_name': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'character_user'", 'primary_key': 'True', 'to': "orm['auth.User']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
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

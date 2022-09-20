# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'NewGame'
        db.create_table('newgame_newgame', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='regist_user', primary_key=True, to=orm['auth.User'])),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, blank=True)),
            ('host_address', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('character_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('nick_name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('sex', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('nation_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image_width', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('image_height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('image_link_url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image_copyright', self.gf('django.db.models.fields.CharField')(max_length=180, blank=True)),
            ('install_class_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('race_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('guardian_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('weapon_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('unique_name', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('activate', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('newgame', ['NewGame'])


    def backwards(self, orm):
        
        # Deleting model 'NewGame'
        db.delete_table('newgame_newgame')


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 15, 13, 20, 7, 651000)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 4, 15, 13, 20, 7, 651000)'}),
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
        'newgame.newgame': {
            'Meta': {'object_name': 'NewGame'},
            'activate': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'character_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'guardian_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'host_address': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'image_copyright': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            'image_height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'image_link_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'image_width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'install_class_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'nation_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'nick_name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'race_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'sex': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'unique_name': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'regist_user'", 'primary_key': 'True', 'to': "orm['auth.User']"}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'weapon_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['newgame']

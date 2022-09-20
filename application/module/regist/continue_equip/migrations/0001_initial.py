# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ContinueEquip'
        db.create_table('continue_equip_continueequip', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], primary_key=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, blank=True)),
            ('host_address', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('install', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('secondary_install', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('equip_main', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('equip_sub', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('equip_head', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('equip_body', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('equip_acce1', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('formation', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('continue_equip', ['ContinueEquip'])


    def backwards(self, orm):
        
        # Deleting model 'ContinueEquip'
        db.delete_table('continue_equip_continueequip')


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 26, 21, 0, 9, 554000)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 6, 26, 21, 0, 9, 554000)'}),
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
        'continue_equip.continueequip': {
            'Meta': {'object_name': 'ContinueEquip'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'equip_acce1': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'equip_body': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'equip_head': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'equip_main': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'equip_sub': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'formation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'host_address': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'install': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'secondary_install': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'primary_key': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'})
        }
    }

    complete_apps = ['continue_equip']

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ContinueShopping'
        db.create_table('continue_trade_continueshopping', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, blank=True)),
            ('host_address', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('shop_act', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('shopping_no', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item_no', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('continue_trade', ['ContinueShopping'])

        # Adding model 'ContinueTrade'
        db.create_table('continue_trade_continuetrade', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, blank=True)),
            ('host_address', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('trade_no', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('trade_entry', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('trade_item_no', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('trade_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('trade_message', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('trade_speed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('continue_trade', ['ContinueTrade'])


    def backwards(self, orm):
        
        # Deleting model 'ContinueShopping'
        db.delete_table('continue_trade_continueshopping')

        # Deleting model 'ContinueTrade'
        db.delete_table('continue_trade_continuetrade')


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 1, 4, 52, 6, 512000)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 1, 4, 52, 6, 512000)'}),
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
        'continue_trade.continueshopping': {
            'Meta': {'object_name': 'ContinueShopping'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'host_address': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'item_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shop_act': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'shopping_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'})
        },
        'continue_trade.continuetrade': {
            'Meta': {'object_name': 'ContinueTrade'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'host_address': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'trade_entry': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trade_item_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trade_message': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'trade_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trade_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trade_speed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'})
        }
    }

    complete_apps = ['continue_trade']

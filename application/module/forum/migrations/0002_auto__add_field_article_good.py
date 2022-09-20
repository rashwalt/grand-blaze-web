# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.good'
        db.add_column('forum_article', 'good',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.good'
        db.delete_column('forum_article', 'good')


    models = {
        'forum.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'delete_mean': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'delete_user_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'edit_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 11, 0, 0)'}),
            'edit_mean': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'forum_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'good': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_delete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'thread_thread'", 'to': "orm['forum.Thread']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'forum.forum': {
            'Meta': {'object_name': 'Forum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'parent_forum': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parent_forum_forum'", 'null': 'True', 'to': "orm['forum.Forum']"})
        },
        'forum.forumstatus': {
            'Meta': {'object_name': 'ForumStatus'},
            'forum': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'forum_forum_status'", 'to': "orm['forum.Forum']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_new_thread': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_thread_rock': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'forum.thread': {
            'Meta': {'object_name': 'Thread'},
            'create_user_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'forum': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'forum_forum'", 'to': "orm['forum.Forum']"}),
            'forum_status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'forum_status_forum_status'", 'to': "orm['forum.ForumStatus']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_rock': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_article_update_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 9, 11, 0, 0)'}),
            'thread_solid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'view_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['forum']
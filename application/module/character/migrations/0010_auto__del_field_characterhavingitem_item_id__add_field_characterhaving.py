# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'CharacterHavingItem.item_id'
        db.delete_column('character_characterhavingitem', 'item_id')

        # Adding field 'CharacterHavingItem.item_v'
        db.add_column('character_characterhavingitem', 'item_v', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['item.Item']), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'CharacterHavingItem.item_id'
        db.add_column('character_characterhavingitem', 'item_id', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Deleting field 'CharacterHavingItem.item_v'
        db.delete_column('character_characterhavingitem', 'item_v_id')


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 9, 1, 28, 41, 711000)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 9, 1, 28, 41, 711000)'}),
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
            'last_update': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 9, 1, 28, 38, 770000)'}),
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
        'character.characteraction': {
            'Meta': {'object_name': 'CharacterAction'},
            'action': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'action_no': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True'}),
            'action_target': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perks_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'character.characterbattle': {
            'Meta': {'object_name': 'CharacterBattle'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'exp_unit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'formation': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'hp': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '0'}),
            'install': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'levelup_point': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'mp': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '0'}),
            'second_install': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'primary_key': 'True'})
        },
        'character.characterhavingitem': {
            'Meta': {'object_name': 'CharacterHavingItem'},
            'box_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'equip_spot': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'have_no': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_new': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'it_box_baz_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_box_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'it_effect': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'it_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'it_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '13', 'decimal_places': '1', 'blank': 'True'}),
            'it_seller': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '13', 'decimal_places': '1', 'blank': 'True'}),
            'item_v': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['item.Item']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'character.characterhavingskill': {
            'Meta': {'object_name': 'CharacterHavingSkill'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_new': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sc_flg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'skill_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'character.charactericon': {
            'Meta': {'object_name': 'CharacterIcon'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'icon_copyright': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'icon_id': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True'}),
            'icon_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'character.characterinstall': {
            'Meta': {'object_name': 'CharacterInstall'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'install_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'character.characterkeyitem': {
            'Meta': {'object_name': 'CharacterKeyItem'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyitem_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'character.charactermovingmark': {
            'Meta': {'object_name': 'CharacterMovingMark'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mark_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'character.characterquest': {
            'Meta': {'object_name': 'CharacterQuest'},
            'clear_fg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quest_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'step': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'character.characterserif': {
            'Meta': {'object_name': 'CharacterSerif'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perks_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'serif_text': ('django.db.models.fields.TextField', [], {}),
            'situation_id': ('django.db.models.fields.IntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'word_no': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'item.item': {
            'Meta': {'object_name': 'Item'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'it_air': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_attack_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_bind': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'it_both_hand': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'it_break': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_charge': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'it_critical': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_dark': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_earth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_equip_install': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'it_equip_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_equip_parts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'it_fire': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_freeze': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_holy': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_metal': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_ok_race': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_ok_sex': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_physics': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_physics_parry': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_pierce': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '13', 'decimal_places': '1'}),
            'it_quest': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'it_range': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_rare': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'it_seller': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '13', 'decimal_places': '1'}),
            'it_shop': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_slash': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_sorcery': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_sorcery_parry': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_stack': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_strike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_sub_category': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_target_area': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_thunder': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_use_item': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'it_water': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['character']

# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HNCommentsTree'
        db.create_table(u'reader_hncommentstree', (
            ('id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('story_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, max_length=10, null=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
            ('hiddenpercent', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, max_length=10)),
            ('hiddencolor', self.gf('django.db.models.fields.CharField')(default='#000000', max_length=7)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('cache', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children', null=True, to=orm['reader.HNCommentsTree'])),
            ('dead', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'reader', ['HNCommentsTree'])


    def backwards(self, orm):
        # Deleting model 'HNCommentsTree'
        db.delete_table(u'reader_hncommentstree')


    models = {
        u'reader.hncomments': {
            'Meta': {'object_name': 'HNComments'},
            'cache': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'dead': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hiddencolor': ('django.db.models.fields.CharField', [], {'default': "'#000000'", 'max_length': '7'}),
            'hiddenpercent': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '10'}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['reader.HNComments']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'story_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '10', 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'reader.hncommentscache': {
            'Meta': {'object_name': 'HNCommentsCache'},
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'reader.hncommentstree': {
            'Meta': {'object_name': 'HNCommentsTree'},
            'cache': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'dead': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hiddencolor': ('django.db.models.fields.CharField', [], {'default': "'#000000'", 'max_length': '7'}),
            'hiddenpercent': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '10'}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'null': 'True', 'to': u"orm['reader.HNCommentsTree']"}),
            'story_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '10', 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'reader.poll': {
            'Meta': {'object_name': 'Poll'},
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'score': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5'}),
            'story_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'max_length': '10', 'null': 'True'})
        },
        u'reader.stories': {
            'Meta': {'object_name': 'Stories'},
            'cache': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5'}),
            'dead': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'score': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '5'}),
            'selfpost': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'selfpost_text': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'story_type': ('django.db.models.fields.CharField', [], {'default': "'news'", 'max_length': '30'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2083'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'})
        },
        u'reader.storycache': {
            'Meta': {'object_name': 'StoryCache'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'over': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'reader.userinfo': {
            'Meta': {'object_name': 'UserInfo'},
            'about': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'avg': ('django.db.models.fields.DecimalField', [], {'default': "''", 'null': 'True', 'max_digits': '20', 'decimal_places': '2'}),
            'cache': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'karma': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '150', 'primary_key': 'True'})
        }
    }

    complete_apps = ['reader']
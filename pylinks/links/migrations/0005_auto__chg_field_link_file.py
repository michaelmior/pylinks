# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Link.file'
        db.alter_column(u'links_link', 'file', self.gf('django.db.models.fields.files.FileField')(max_length=500, null=True))

    def backwards(self, orm):

        # Changing field 'Link.file'
        db.alter_column(u'links_link', 'file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

    models = {
        u'links.category': {
            'Meta': {'object_name': 'Category'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'links.link': {
            'Meta': {'object_name': 'Link'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links'", 'null': 'True', 'to': u"orm['links.Category']"}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '500', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'visits': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['links']
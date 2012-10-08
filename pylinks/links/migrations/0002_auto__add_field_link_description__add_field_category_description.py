# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Link.description'
        db.add_column('links_link', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Adding field 'Category.description'
        db.add_column('links_category', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Link.description'
        db.delete_column('links_link', 'description')

        # Deleting field 'Category.description'
        db.delete_column('links_category', 'description')


    models = {
        'links.category': {
            'Meta': {'object_name': 'Category'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        'links.link': {
            'Meta': {'object_name': 'Link'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links'", 'null': 'True', 'to': "orm['links.Category']"}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['links']
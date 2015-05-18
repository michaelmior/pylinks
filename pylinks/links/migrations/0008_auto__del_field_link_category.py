# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Link.category'
        db.delete_column(u'links_link', 'category_id')


    def backwards(self, orm):
        # Adding field 'Link.category'
        db.add_column(u'links_link', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='links', null=True, to=orm['links.Category']),
                      keep_default=False)


    models = {
        u'links.category': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Category'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'links.link': {
            'Meta': {'object_name': 'Link'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['links.Category']", 'symmetrical': 'False'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'default': 'None', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'visits': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['links']
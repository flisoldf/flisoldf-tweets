# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HashTags'
        db.create_table('hashtags', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('hashtag', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('configurations', ['HashTags'])

    def backwards(self, orm):
        # Deleting model 'HashTags'
        db.delete_table('hashtags')

    models = {
        'configurations.hashtags': {
            'Meta': {'object_name': 'HashTags', 'db_table': "'hashtags'"},
            'hashtag': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['configurations']
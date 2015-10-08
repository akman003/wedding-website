# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Invitee'
        db.create_table(u'rsvps_invitee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('num_allowed', self.gf('django.db.models.fields.IntegerField')()),
            ('was_submitted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('num_rsvpd', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'rsvps', ['Invitee'])

        # Adding model 'RSVPLog'
        db.create_table(u'rsvps_rsvplog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invitee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsvps.Invitee'])),
            ('ip_address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('num_rsvpd', self.gf('django.db.models.fields.IntegerField')()),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'rsvps', ['RSVPLog'])


    def backwards(self, orm):
        # Deleting model 'Invitee'
        db.delete_table(u'rsvps_invitee')

        # Deleting model 'RSVPLog'
        db.delete_table(u'rsvps_rsvplog')


    models = {
        u'rsvps.invitee': {
            'Meta': {'object_name': 'Invitee'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'num_allowed': ('django.db.models.fields.IntegerField', [], {}),
            'num_rsvpd': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'was_submitted': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'rsvps.rsvplog': {
            'Meta': {'ordering': "['-timestamp']", 'object_name': 'RSVPLog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsvps.Invitee']"}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'num_rsvpd': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rsvps']
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('notifications', '0005_auto_20151123_0103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationevent',
            old_name='id_cible',
            new_name='accessory_id',
        ),
        migrations.RenameField(
            model_name='notificationevent',
            old_name='prevenu_par_email',
            new_name='emailed',
        ),
        migrations.RenameField(
            model_name='notificationevent',
            old_name='lue',
            new_name='read',
        ),
        migrations.RenameField(
            model_name='notificationevent',
            old_name='vue',
            new_name='seen',
        ),
        migrations.RenameField(
            model_name='notificationevent',
            old_name='id_acteur',
            new_name='sender_id',
        ),
        migrations.RemoveField(
            model_name='notificationevent',
            name='destinataire',
        ),
        migrations.RemoveField(
            model_name='notificationevent',
            name='id_lieu',
        ),
        migrations.RemoveField(
            model_name='notificationevent',
            name='type_acteur',
        ),
        migrations.RemoveField(
            model_name='notificationevent',
            name='type_cible',
        ),
        migrations.RemoveField(
            model_name='notificationevent',
            name='type_lieu',
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='accessory_type',
            field=models.ForeignKey(blank=True, null=True, related_name='notification_accessory', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='recipient',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='sender_type',
            field=models.ForeignKey(blank=True, null=True, related_name='notification_sender', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='target_id',
            field=models.CharField(null=True, blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='target_type',
            field=models.ForeignKey(blank=True, null=True, related_name='notification_target', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='notificationevent',
            name='category',
            field=models.CharField(default='OLD', choices=[('WELCOME', 'A new user has joined'), ('NEW_POST', 'A post has been created'), ('UVPOTED', 'A post has been upvoted'), ('NEW_REPLY_TO_POST', 'Someone has replied to a post'), ('NEW_REPLY_TO_COMMENT', 'Someone has replied to a comment'), ('CHANNEL_JOIN_REQUEST', 'Someone wants to join a channel'), ('CHANNEL_JOIN_REQUEST_DENIED', 'A request to join a channel has been denied'), ('CHANNEL_JOIN_REQUEST_ACCEPTED', 'A request to join a channel has been accepted'), ('OLD', 'A legacy notification'), ('TEST', 'A test notification')], max_length=255),
        ),
    ]

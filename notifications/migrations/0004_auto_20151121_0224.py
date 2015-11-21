# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20151121_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationevent',
            name='action',
        ),
        migrations.AlterField(
            model_name='notificationevent',
            name='category',
            field=models.CharField(choices=[('WELCOME', 'A new user has joined'), ('NEW_POST', 'A post has been created'), ('UVPOTED', 'A post has been upvoted'), ('NEW_REPLY_TO_POST', 'Someone has replied to a post'), ('NEW_REPLY_TO_COMMENT', 'Someone has replied to a comment'), ('CHANNEL_JOIN_REQUEST', 'Someone wants to join a channel'), ('CHANNEL_JOIN_REQUEST_DENIED', 'A request to join a channel has been denied'), ('CHANNEL_JOIN_REQUEST_ACCEPTED', 'A request to join a channel has been accepted'), ('OLD', 'A legacy notification')], default='OLD', max_length=255),
        ),
    ]

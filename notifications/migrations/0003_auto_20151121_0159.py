# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20151118_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.AddField(
            model_name='notificationevent',
            name='category',
            field=models.CharField(max_length=255, choices=[('WELCOME', 'A new user has joined'), ('NEW_POST', 'A post has been created'), ('UVPOTED', 'A post has been upvoted'), ('NEW_REPLY_TO_POST', 'Someone has replied to a post'), ('NEW_REPLY_TO_COMMENT', 'Someone has replied to a comment'), ('OLD', 'A legacy notification')], default='OLD'),
        ),
    ]

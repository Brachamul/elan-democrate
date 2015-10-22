# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aggregateur', '0012_auto_20151006_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='WantToJoinChannel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='channel',
            name='want_to_join',
        ),
        migrations.AddField(
            model_name='wanttojoinchannel',
            name='channel',
            field=models.ForeignKey(to='aggregateur.Channel'),
        ),
        migrations.AddField(
            model_name='wanttojoinchannel',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

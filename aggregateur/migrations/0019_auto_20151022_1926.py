# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0018_settings_main_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='WelcomeText',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('content', models.TextField(max_length=1024)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.DeleteModel(
            name='Settings',
        ),
    ]

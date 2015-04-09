# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aggregateur', '0007_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastRanking',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

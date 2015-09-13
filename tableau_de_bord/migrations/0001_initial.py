# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('template', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('destination', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

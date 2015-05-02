# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mandats', '0002_auto_20150422_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='detenteur',
            name='id',
            field=models.AutoField(auto_created=True, default=1, verbose_name='ID', primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detenteur',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

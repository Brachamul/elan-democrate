# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_with_one_time_code', '0007_auto_20150916_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='code',
            field=models.CharField(default='0NQV39', max_length=6),
        ),
        migrations.AlterField(
            model_name='emailconfirmationinstance',
            name='code',
            field=models.CharField(default='6K5BGCDCHL1XK5XUKOXLATL6FUCUNIJ5', max_length=32),
        ),
    ]

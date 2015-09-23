# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import auth_with_one_time_code.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_with_one_time_code', '0009_auto_20150922_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='code',
            field=models.CharField(max_length=6, default=auth_with_one_time_code.models.credentials_code),
        ),
        migrations.AlterField(
            model_name='emailconfirmationinstance',
            name='code',
            field=models.CharField(max_length=32, default=auth_with_one_time_code.models.email_confirmation_code),
        ),
    ]

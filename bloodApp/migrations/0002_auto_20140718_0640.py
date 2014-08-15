# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bloodApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='userContact',
            field=models.IntegerField(max_length=10),
        ),
    ]

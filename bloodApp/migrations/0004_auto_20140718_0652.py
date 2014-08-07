# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('bloodApp', '0003_auto_20140718_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userContact',
            field=models.IntegerField(unique=True, max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message=b'Length has to be 10', code=b'Invalid number')]),
        ),
    ]

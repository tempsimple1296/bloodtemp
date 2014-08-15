# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('bloodApp', '0005_auto_20140718_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userAge',
            field=models.IntegerField(default=18, max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='userContact',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(b'^[0-9]+$', b'Enter a valid phone number.')]),
        ),
    ]

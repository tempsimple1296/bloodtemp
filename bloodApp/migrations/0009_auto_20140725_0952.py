# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('bloodApp', '0008_auto_20140725_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userBloodGroup',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(b'^(A|B|AB|O|a|b|ab|o)[+-]$', b'Enter A Valid Human BloodGroup..!!!')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='userContact',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(b'^[0-9]+$', b'Enter a valid phone number.')]),
        ),
    ]

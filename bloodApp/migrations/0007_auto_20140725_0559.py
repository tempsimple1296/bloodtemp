# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('bloodApp', '0006_auto_20140718_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userBloodGroup',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(b'^(A|B|AB|O|a|b|ab|o)[+-]$', b'Enter A Valid Human BloodGroup..!!!')]),
        ),
    ]

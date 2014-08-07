# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloodApp', '0007_auto_20140725_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userBloodGroup',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='userContact',
            field=models.CharField(max_length=10),
        ),
    ]

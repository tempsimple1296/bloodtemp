# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userName', models.CharField(max_length=50)),
                ('userLoc', models.CharField(max_length=30)),
                ('userAge', models.IntegerField(default=18)),
                ('userContact', models.IntegerField()),
                ('userBloodGroup', models.CharField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

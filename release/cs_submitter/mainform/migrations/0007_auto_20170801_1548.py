# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainform', '0006_auto_20170801_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='day',
            field=models.CharField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday')], max_length=8),
        ),
    ]

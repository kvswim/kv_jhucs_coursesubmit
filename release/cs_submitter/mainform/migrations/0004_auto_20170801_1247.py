# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainform', '0003_auto_20170801_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainformmodel',
            name='days_of_week',
            field=models.CharField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday')], max_length=8),
        ),
    ]

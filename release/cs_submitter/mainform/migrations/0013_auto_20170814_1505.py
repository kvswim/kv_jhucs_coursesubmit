# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainform', '0012_auto_20170808_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainformmodel',
            name='is_new_course',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mainformmodel',
            name='section_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mainformmodel',
            name='course_instructor',
            field=models.CharField(choices=[('', 'Pick a faculty'), ('STAFF', 'Staff'), ('Ahmad, Yanif', 'Ahmad, Yanif'), ('Amir, Yair', 'Amir, Yair'), ('Arora, Raman', 'Arora, Raman'), ('Battle, Alexis', 'Battle, Alexis'), ('Braverman, Vladimir', 'Braverman, Vladimir'), ('Burns, Randal', 'Burns, Randal'), ('Dahbura, Anton', 'Dahbura, Anton'), ('Dinitz, Michael', 'Dinitz, Michael'), ('Drezde, Mark', 'Drezde, Mark'), ('Duh, Kevin', 'Duh, Kevin'), ('Eisner, Jason', 'Eisner, Jason'), ('Froehlich, Peter', 'Froehlich, Peter'), ('Green, Matthew', 'Green, Matthew'), ('Hager, Gregory', 'Hager, Gregory'), ('Hohenberger, Susan', 'Hohenberger, Susan'), ('Huang, Ryan (Peng)', 'Huang, Ryan (Peng)'), ('Jain, Abhishek', 'Jain, Abhishek'), ('Jin, Xin', 'Jin, Xin'), ('Kazanzides, Peter', 'Kazanzides, Peter'), ('Kazhdan, Michael', 'Kazhdan, Michael'), ('Koehn, Philipp', 'Koehn, Philipp'), ('Kosaraju, S. Rao', 'Kosaraju, S. Rao'), ('Langmead, Benjamin', 'Langmead, Benjamin'), ('Leonard, Simon', 'Leonard, Simon'), ('Li, Xin', 'Li, Xin'), ('Masson, Gerald', 'Masson, Gerald'), ('Miner More, Sara', 'Miner More, Sara'), ('Navab, Nassir', 'Navab, Nassir'), ('Reiter, Austin', 'Reiter, Austin'), ('Rubin, Aviel', 'Rubin, Aviel'), ('Salzberg, Steven', 'Salzberg, Steven'), ('Saria, Suchi', 'Saria, Suchi'), ('Schatz, Michael', 'Schatz, Michael'), ('Selinski, Joanne', 'Selinski, Joanne'), ('Shpitser, Ilya', 'Shpitser, Ilya'), ('Smith, Scott', 'Smith, Scott'), ('Szalay, Alex', 'Szalay, Alex'), ('Taylor, Rusell', 'Taylor, Rusell'), ('Terzis, Andreas', 'Terzis, Andreas'), ('Van Durme, Benjamin', 'Van Durme, Benjamin'), ('Yarowsky, David', 'Yarowsky, David'), ('Yuille, Alan', 'Yuille, Alan')], max_length=255),
        ),
        migrations.AlterField(
            model_name='mainformmodel',
            name='semester',
            field=models.CharField(choices=[('', 'Pick a semester'), ('F', 'Fall 2017'), ('S', 'Spring 2018')], max_length=12),
        ),
    ]

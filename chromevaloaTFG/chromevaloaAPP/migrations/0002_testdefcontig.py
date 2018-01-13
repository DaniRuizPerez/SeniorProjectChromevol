# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chromevaloaAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestDefContig',
            fields=[
                ('idcontig', models.CharField(max_length=100, serialize=False, primary_key=True, db_column='IDcontig')),
                ('descrip', models.TextField()),
                ('accession', models.CharField(max_length=100)),
                ('length', models.IntegerField()),
                ('evalue', models.FloatField()),
                ('identity', models.FloatField()),
                ('goprocess', models.TextField(db_column='GOProcess')),
                ('gofunction', models.TextField(db_column='GOFunction')),
                ('gocompartment', models.TextField(db_column='GOCompartment')),
                ('ec', models.TextField(db_column='EC')),
                ('ips', models.TextField(db_column='IPS')),
                ('numreads', models.IntegerField()),
                ('selected', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'test_def_contig',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]

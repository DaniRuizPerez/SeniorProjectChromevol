# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllUnigenes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idcontig', models.CharField(max_length=100, db_column='IDcontig')),
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
                'db_table': 'all_unigenes',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField()),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=75)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('idcluster', models.CharField(max_length=100, serialize=False, primary_key=True, db_column='IDcluster')),
                ('idcontig', models.CharField(max_length=100, db_column='IDcontig')),
                ('clusterseq', models.TextField(db_column='clusterSEQ')),
            ],
            options={
                'db_table': 'cluster',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cluster2',
            fields=[
                ('idcluster', models.CharField(max_length=100, serialize=False, primary_key=True, db_column='IDcluster')),
                ('clusterseq', models.TextField(db_column='clusterSEQ')),
            ],
            options={
                'db_table': 'cluster2',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contig',
            fields=[
                ('idcontig', models.CharField(max_length=100, serialize=False, primary_key=True, db_column='IDcontig')),
                ('contigseq', models.TextField(db_column='contigSEQ')),
            ],
            options={
                'db_table': 'contig',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contig2',
            fields=[
                ('idcontig', models.CharField(max_length=100, serialize=False, primary_key=True, db_column='IDcontig')),
                ('descrip', models.TextField()),
                ('evalue', models.FloatField()),
                ('identity', models.CharField(max_length=50)),
                ('numreads', models.IntegerField()),
                ('seq', models.TextField()),
            ],
            options={
                'db_table': 'contig2',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contigs',
            fields=[
                ('id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('descrip', models.CharField(max_length=500)),
                ('seq', models.TextField()),
            ],
            options={
                'db_table': 'contigs',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contigseq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idcontig', models.CharField(max_length=100, db_column='IDcontig')),
                ('contigseq', models.TextField(db_column='contigSEQ')),
            ],
            options={
                'db_table': 'contigseq',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DefContig',
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
                'db_table': 'def_contig',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DefNormMgcReadCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acc', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'DEF_NORM_MGC_read_count',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DefNormMgtReadCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acc', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'DEF_NORM_MGT_read_count',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.CharField(max_length=100, serialize=False, primary_key=True, db_column='ID')),
                ('expr', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'expression',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fulllengther',
            fields=[
                ('idcontig', models.CharField(max_length=50, serialize=False, primary_key=True, db_column='IDcontig')),
                ('result', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'fulllengther',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fulllengther2',
            fields=[
                ('idcontig', models.CharField(max_length=50, serialize=False, primary_key=True, db_column='IDcontig')),
                ('result', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'fulllengther2',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genes',
            fields=[
                ('accession', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('idgene', models.CharField(unique=True, max_length=250, db_column='IDgene')),
                ('goprocess', models.TextField(db_column='GOprocess')),
                ('gofunction', models.TextField(db_column='GOfunction')),
                ('gocompartment', models.TextField(db_column='GOcompartment')),
            ],
            options={
                'db_table': 'genes',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gocodes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seqid', models.CharField(max_length=50, db_column='seqID')),
                ('gocode', models.CharField(max_length=50, db_column='GOcode')),
            ],
            options={
                'db_table': 'GOcodes',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Read',
            fields=[
                ('idread', models.CharField(max_length=100, serialize=False, primary_key=True, db_column='IDread')),
                ('idcluster', models.CharField(max_length=100, db_column='IDcluster', blank=True)),
                ('readseq', models.TextField(db_column='readSEQ')),
            ],
            options={
                'db_table': 'read',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Read2',
            fields=[
                ('idread', models.CharField(max_length=100, serialize=False, primary_key=True, db_column='IDread')),
                ('readseq', models.TextField(db_column='readSEQ')),
            ],
            options={
                'db_table': 'read2',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SelContigTable',
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
                'db_table': 'sel_contig_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SelDeUnigeneTable',
            fields=[
                ('id', models.CharField(max_length=100, serialize=False, primary_key=True, db_column='ID')),
                ('expr', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'sel_DE_unigene_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SelectedContig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idcontig', models.CharField(max_length=100, db_column='IDcontig')),
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
                'db_table': 'selected_contig',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SelectedOver80Id',
            fields=[
                ('id', models.CharField(max_length=100, serialize=False, primary_key=True, db_column='ID')),
            ],
            options={
                'db_table': 'selected_over80id',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SelectedUnigene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idcontig', models.CharField(max_length=100, db_column='IDcontig')),
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
                'db_table': 'selected_unigene',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SelUnigeneBuena',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idcontig', models.CharField(max_length=100, db_column='IDcontig')),
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
                'db_table': 'sel_unigene_buena',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SelUnigeneTable',
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
                'db_table': 'sel_unigene_table',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TransientUnigene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idcontig', models.CharField(max_length=100, db_column='IDcontig')),
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
                'db_table': 'transient_unigene',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TransientUnigeneAll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idcontig', models.CharField(max_length=100, db_column='IDcontig')),
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
                'db_table': 'transient_unigene_all',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TransientUnigeneSelected',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idcontig', models.CharField(max_length=100, db_column='IDcontig')),
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
                'db_table': 'transient_unigene_selected',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]

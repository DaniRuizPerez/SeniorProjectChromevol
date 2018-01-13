# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Cluster2(models.Model):
    idcluster = models.CharField(db_column='IDcluster', primary_key=True, max_length=100)  # Field name made lowercase.
    idcontig = models.CharField(db_column='IDcontig', max_length=100)  # Field name made lowercase.
    clusterseq = models.TextField(db_column='clusterSEQ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster2'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Expression(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=100)  # Field name made lowercase.
    expr = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'expression'


class Fulllengther2(models.Model):
    idcontig = models.CharField(db_column='IDcontig', primary_key=True, max_length=50)  # Field name made lowercase.
    result = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'fulllengther2'


class Read2(models.Model):
    idread = models.CharField(db_column='IDread', primary_key=True, max_length=100)  # Field name made lowercase.
    idcluster = models.CharField(db_column='IDcluster', max_length=100)  # Field name made lowercase.
    readseq = models.TextField(db_column='readSEQ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'read2'


class SelContigTable(models.Model):
    idcontig = models.CharField(db_column='IDcontig', primary_key=True, max_length=100)  # Field name made lowercase.
    result = models.CharField(max_length=50)
    descrip = models.TextField()
    accession = models.CharField(max_length=100)
    length = models.IntegerField()
    evalue = models.FloatField()
    identity = models.FloatField()
    goprocess = models.TextField(db_column='GOProcess')  # Field name made lowercase.
    gofunction = models.TextField(db_column='GOFunction')  # Field name made lowercase.
    gocompartment = models.TextField(db_column='GOCompartment')  # Field name made lowercase.
    ec = models.TextField(db_column='EC')  # Field name made lowercase.
    ips = models.TextField(db_column='IPS')  # Field name made lowercase.
    numreads = models.IntegerField()
    selected = models.CharField(max_length=1)
    contigseq = models.TextField(db_column='contigSEQ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sel_contig_table'


class SelUnigeneTable(models.Model):
    idcontig = models.CharField(db_column='IDcontig', primary_key=True, max_length=100)  # Field name made lowercase.
    descrip = models.TextField()
    accession = models.CharField(max_length=100)
    length = models.IntegerField()
    evalue = models.FloatField()
    identity = models.FloatField()
    goprocess = models.TextField(db_column='GOProcess')  # Field name made lowercase.
    gofunction = models.TextField(db_column='GOFunction')  # Field name made lowercase.
    gocompartment = models.TextField(db_column='GOCompartment')  # Field name made lowercase.
    ec = models.TextField(db_column='EC')  # Field name made lowercase.
    ips = models.TextField(db_column='IPS')  # Field name made lowercase.
    numreads = models.IntegerField()
    selected = models.CharField(max_length=1)
    expr = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sel_unigene_table'









'''

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.


from __future__ import unicode_literals

from django.db import models


class DefNormMgcReadCount(models.Model):
    acc = models.CharField(max_length=100)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DEF_NORM_MGC_read_count'


class DefNormMgtReadCount(models.Model):
    acc = models.CharField(max_length=100)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DEF_NORM_MGT_read_count'


class Gocodes(models.Model):
    seqid = models.CharField(db_column='seqID', max_length=50)  # Field name made lowercase.
    gocode = models.CharField(db_column='GOcode', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GOcodes'


class AllUnigenes(models.Model):
    idcontig = models.CharField(db_column='IDcontig', max_length=100)  # Field name made lowercase.
    descrip = models.TextField()
    accession = models.CharField(max_length=100)
    length = models.IntegerField()
    evalue = models.FloatField()
    identity = models.FloatField()
    goprocess = models.TextField(db_column='GOProcess')  # Field name made lowercase.
    gofunction = models.TextField(db_column='GOFunction')  # Field name made lowercase.
    gocompartment = models.TextField(db_column='GOCompartment')  # Field name made lowercase.
    ec = models.TextField(db_column='EC')  # Field name made lowercase.
    ips = models.TextField(db_column='IPS')  # Field name made lowercase.
    numreads = models.IntegerField()
    selected = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'all_unigenes'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Cluster(models.Model):
    idcluster = models.CharField(db_column='IDcluster', primary_key=True, max_length=100)  # Field name made lowercase.
    idcontig = models.CharField(db_column='IDcontig', max_length=100)  # Field name made lowercase.
    clusterseq = models.TextField(db_column='clusterSEQ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster'


class Cluster2(models.Model):
    idcluster = models.CharField(db_column='IDcluster', primary_key=True, max_length=100)  # Field name made lowercase.
    idcontig = models.ForeignKey('DefContig', db_column='IDcontig')  # Field name made lowercase.
    clusterseq = models.TextField(db_column='clusterSEQ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cluster2'


class Contig(models.Model):
    idcontig = models.CharField(db_column='IDcontig', primary_key=True, max_length=100)  # Field name made lowercase.
    contigseq = models.TextField(db_column='contigSEQ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contig'


class Contig2(models.Model):
    idcontig = models.CharField(db_column='IDcontig', primary_key=True, max_length=100)  # Field name made lowercase.
    descrip = models.TextField()
    evalue = models.FloatField()
    identity = models.CharField(max_length=50)
    numreads = models.IntegerField()
    seq = models.TextField()

    class Meta:
        managed = False
        db_table = 'contig2'


class Contigs(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    descrip = models.CharField(max_length=500)
    seq = models.TextField()

    class Meta:
        managed = False
        db_table = 'contigs'


class Contigseq(models.Model):
    idcontig = models.CharField(db_column='IDcontig', max_length=100)  # Field name made lowercase.
    contigseq = models.TextField(db_column='contigSEQ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contigseq'


class DefContig(models.Model):
    idcontig = models.CharField(db_column='IDcontig', primary_key=True, max_length=100)  # Field name made lowercase.
    descrip = models.TextField()
    accession = models.CharField(max_length=100)
    length = models.IntegerField()
    evalue = models.FloatField()
    identity = models.FloatField()
    goprocess = models.TextField(db_column='GOProcess')  # Field name made lowercase.
    gofunction = models.TextField(db_column='GOFunction')  # Field name made lowercase.
    gocompartment = models.TextField(db_column='GOCompartment')  # Field name made lowercase.
    ec = models.TextField(db_column='EC')  # Field name made lowercase.
    ips = models.TextField(db_column='IPS')  # Field name made lowercase.
    numreads = models.IntegerField()
    selected = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'def_contig'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Expression(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=100)  # Field name made lowercase.
    expr = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'expression'



class Fulllengther(models.Model):
    idcontig = models.CharField(db_column='IDcontig', primary_key=True, max_length=50)  # Field name made lowercase.
    result = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'fulllengther'


class Fulllengther2(models.Model):
    idcontig = models.CharField(db_column='IDcontig', primary_key=True, max_length=50)  # Field name made lowercase.
    result = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'fulllengther2'


class Genes(models.Model):
    accession = models.CharField(primary_key=True, max_length=50)
    idgene = models.CharField(db_column='IDgene', unique=True, max_length=250)  # Field name made lowercase.
    goprocess = models.TextField(db_column='GOprocess')  # Field name made lowercase.
    gofunction = models.TextField(db_column='GOfunction')  # Field name made lowercase.
    gocompartment = models.TextField(db_column='GOcompartment')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'genes'


class Read(models.Model):
    idread = models.CharField(db_column='IDread', primary_key=True, max_length=100)  # Field name made lowercase.
    idcluster = models.CharField(db_column='IDcluster', max_length=100, blank=True)  # Field name made lowercase.
    readseq = models.TextField(db_column='readSEQ')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'read'


class Read2(models.Model):
    idread = models.CharField(db_column='IDread', primary_key=True, max_length=100)  # Field name made lowercase.
    idcluster = models.ForeignKey(Cluster2, db_column='IDcluster')  # Field name made lowercase.
    readseq = models.TextField(db_column='readSEQ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'read2'



class SelDeUnigeneTable(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=100)  # Field name made lowercase.
    expr = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'sel_DE_unigene_table'


class SelContigTable(models.Model):
    idcontig = models.CharField(db_column='IDcontig', primary_key=True, max_length=100)  # Field name made lowercase.
    descrip = models.TextField()
    accession = models.CharField(max_length=100)
    length = models.IntegerField()
    evalue = models.FloatField()
    identity = models.FloatField()
    goprocess = models.TextField(db_column='GOProcess')  # Field name made lowercase.
    gofunction = models.TextField(db_column='GOFunction')  # Field name made lowercase.
    gocompartment = models.TextField(db_column='GOCompartment')  # Field name made lowercase.
    ec = models.TextField(db_column='EC')  # Field name made lowercase.
    ips = models.TextField(db_column='IPS')  # Field name made lowercase.
    numreads = models.IntegerField()
    selected = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sel_contig_table'


class SelUnigeneBuena(models.Model):
    idcontig = models.CharField(db_column='IDcontig', max_length=100)  # Field name made lowercase.
    descrip = models.TextField()
    accession = models.CharField(max_length=100)
    length = models.IntegerField()
    evalue = models.FloatField()
    identity = models.FloatField()
    goprocess = models.TextField(db_column='GOProcess')  # Field name made lowercase.
    gofunction = models.TextField(db_column='GOFunction')  # Field name made lowercase.
    gocompartment = models.TextField(db_column='GOCompartment')  # Field name made lowercase.
    ec = models.TextField(db_column='EC')  # Field name made lowercase.
    ips = models.TextField(db_column='IPS')  # Field name made lowercase.
    numreads = models.IntegerField()
    selected = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sel_unigene_buena'


class SelUnigeneTable(models.Model):
    idcontig = models.CharField(db_column='IDcontig', primary_key=True, max_length=100)  # Field name made lowercase.
    descrip = models.TextField()
    accession = models.CharField(max_length=100)
    length = models.IntegerField()
    evalue = models.FloatField()
    identity = models.FloatField()
    goprocess = models.TextField(db_column='GOProcess')  # Field name made lowercase.
    gofunction = models.TextField(db_column='GOFunction')  # Field name made lowercase.
    gocompartment = models.TextField(db_column='GOCompartment')  # Field name made lowercase.
    ec = models.TextField(db_column='EC')  # Field name made lowercase.
    ips = models.TextField(db_column='IPS')  # Field name made lowercase.
    numreads = models.IntegerField()
    selected = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sel_unigene_table'


class SelectedContig(models.Model):
    idcontig = models.CharField(db_column='IDcontig', max_length=100)  # Field name made lowercase.
    descrip = models.TextField()
    accession = models.CharField(max_length=100)
    length = models.IntegerField()
    evalue = models.FloatField()
    identity = models.FloatField()
    goprocess = models.TextField(db_column='GOProcess')  # Field name made lowercase.
    gofunction = models.TextField(db_column='GOFunction')  # Field name made lowercase.
    gocompartment = models.TextField(db_column='GOCompartment')  # Field name made lowercase.
    ec = models.TextField(db_column='EC')  # Field name made lowercase.
    ips = models.TextField(db_column='IPS')  # Field name made lowercase.
    numreads = models.IntegerField()
    selected = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'selected_contig'


class SelectedOver80Id(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'selected_over80id'


class SelectedUnigene(models.Model):
    idcontig = models.CharField(db_column='IDcontig', max_length=100)  # Field name made lowercase.
    descrip = models.TextField()
    accession = models.CharField(max_length=100)
    length = models.IntegerField()
    evalue = models.FloatField()
    identity = models.FloatField()
    goprocess = models.TextField(db_column='GOProcess')  # Field name made lowercase.
    gofunction = models.TextField(db_column='GOFunction')  # Field name made lowercase.
    gocompartment = models.TextField(db_column='GOCompartment')  # Field name made lowercase.
    ec = models.TextField(db_column='EC')  # Field name made lowercase.
    ips = models.TextField(db_column='IPS')  # Field name made lowercase.
    numreads = models.IntegerField()
    selected = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'selected_unigene'


class TransientUnigene(models.Model):
    idcontig = models.CharField(db_column='IDcontig', max_length=100)  # Field name made lowercase.
    descrip = models.TextField()
    accession = models.CharField(max_length=100)
    length = models.IntegerField()
    evalue = models.FloatField()
    identity = models.FloatField()
    goprocess = models.TextField(db_column='GOProcess')  # Field name made lowercase.
    gofunction = models.TextField(db_column='GOFunction')  # Field name made lowercase.
    gocompartment = models.TextField(db_column='GOCompartment')  # Field name made lowercase.
    ec = models.TextField(db_column='EC')  # Field name made lowercase.
    ips = models.TextField(db_column='IPS')  # Field name made lowercase.
    numreads = models.IntegerField()
    selected = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'transient_unigene'


class TransientUnigeneAll(models.Model):
    idcontig = models.CharField(db_column='IDcontig', max_length=100)  # Field name made lowercase.
    descrip = models.TextField()
    accession = models.CharField(max_length=100)
    length = models.IntegerField()
    evalue = models.FloatField()
    identity = models.FloatField()
    goprocess = models.TextField(db_column='GOProcess')  # Field name made lowercase.
    gofunction = models.TextField(db_column='GOFunction')  # Field name made lowercase.
    gocompartment = models.TextField(db_column='GOCompartment')  # Field name made lowercase.
    ec = models.TextField(db_column='EC')  # Field name made lowercase.
    ips = models.TextField(db_column='IPS')  # Field name made lowercase.
    numreads = models.IntegerField()
    selected = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'transient_unigene_all'


class TransientUnigeneSelected(models.Model):
    idcontig = models.CharField(db_column='IDcontig', max_length=100)  # Field name made lowercase.
    descrip = models.TextField()
    accession = models.CharField(max_length=100)
    length = models.IntegerField()
    evalue = models.FloatField()
    identity = models.FloatField()
    goprocess = models.TextField(db_column='GOProcess')  # Field name made lowercase.
    gofunction = models.TextField(db_column='GOFunction')  # Field name made lowercase.
    gocompartment = models.TextField(db_column='GOCompartment')  # Field name made lowercase.
    ec = models.TextField(db_column='EC')  # Field name made lowercase.
    ips = models.TextField(db_column='IPS')  # Field name made lowercase.
    numreads = models.IntegerField()
    selected = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'transient_unigene_selected'

'''
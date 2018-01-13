import django_tables2 as tables
from chromevaloaAPP.models import SelContigTable,SelUnigeneTable
from django_tables2.utils import A #Accessor
from django_tables2.columns import LinkColumn
from django_tables2.columns import TemplateColumn
from django.utils.translation import ugettext as _

from django.conf.urls.static import static
from django.templatetags.static import static

class SelContigTableTable(tables.Table):
    edit = tables.TemplateColumn('<a target = "blank" href=/admin/chromevaloaAPP/selcontigtable/{{record.idcontig}}>'+' \
      <img alt="edit" title="edit"  id = "edit" src="{0}" width="25" height="25"></a>'\
      .format(static("chromevaloaAPP/img/edit.png")),verbose_name= _('EDIT'),sortable=False)

    idcontig = tables.TemplateColumn('<a target=_blank href=/details/{{record.idcontig}}>\
      {{record.idcontig}}</a>',verbose_name= _('CONTIG ID'))
    accession = tables.TemplateColumn('<a target=_blank href=http://www.ncbi.nlm.nih.gov/protein/{{record.accession}}>\
      {{record.accession}}</a>',verbose_name=_('TOP BLAST HIT ACCESSION'))
    descrip = tables.Column(verbose_name= _('DESCRIPTION'))
    numreads = tables.Column(verbose_name= _('NUM. READS'))
    evalue = tables.Column(verbose_name= _('E-VALUE' ))
    identity = tables.Column(verbose_name= _('MEAN SIMILARITY' ))
    #result = tables.Column(verbose_name= _('ORF DESCRIPTION' ))
    result = tables.TemplateColumn('{{record.result|slice:"2:-1"}}',verbose_name=_('ORF DESCRIPTION'))

    class Meta:
        model = SelContigTable
        attrs = {"class": "paleblue1"}
        fields = ('edit','idcontig','descrip','numreads','accession','evalue','identity','result')

class SelUnigeneTableTable(tables.Table):
      edit = tables.TemplateColumn('<a target = "blank" href=/admin/chromevaloaAPP/selunigenetable/{{record.idcontig}}>'+' \
      <img alt="edit" title="edit"  id = "edit" src="{0}" width="25" height="25"></a>'\
      .format(static("chromevaloaAPP/img/edit.png")),verbose_name= _('EDIT'),sortable=False)

      accession = tables.TemplateColumn('<a target=_blank href=http://www.ncbi.nlm.nih.gov/protein/{{record.accession}}>\
        {{record.accession}}</a>',verbose_name= _('TOP HIT ACCESSION'))
      descrip = tables.TemplateColumn('<a target=_blank href=/browse/search/?field=accession&q={{record.accession}}>\
        {{record.descrip}}</a>',verbose_name= _('DESCRIPTION'))
      expr = tables.Column(verbose_name= _('DIFFERENTIAL EXPRESSION' ))

      class Meta:
        model = SelUnigeneTable
        attrs = {"class": "paleblue1"}
        fields = ('edit', 'accession','descrip', 'expr')

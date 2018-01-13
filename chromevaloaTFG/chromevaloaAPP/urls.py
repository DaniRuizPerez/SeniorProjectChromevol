from django.conf.urls import patterns, url
from chromevaloaAPP import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'browse/search/', views.searchBrowse, name='searchBrowse'),
    url(r'browse/getBrowseCSV/', views.getBrowseCSV, name='getBrowseCSV'),
    url(r'browse/', views.browse, name='browse'),
    url(r'blast/programHelp', views.programHelp, name='programHelp'),
    url(r'blast/dbHelp', views.dbHelp, name='dbHelp'),
    url(r'blast/', views.blast, name='blast'),
    url(r'unigenes/', views.browse, name='unigenes'),
    url(r'expressions/search/', views.searchExpression, name='searchExpression'),
    url(r'expressions/getExpressionCSV/', views.getExpressionCSV, name='getExpressionCSV'),
    url(r'expressions/', views.expression, name='expression'),
    url(r'^details/jalview/getAlnFile', views.getAlnFile, name='getAlnFile'),
    url(r'^details/jalview/(?P<contig>\w+)', views.jalview, name='jalview'),
    url(r'^details/(?P<accession>\w+)', views.details, name='details'),
)
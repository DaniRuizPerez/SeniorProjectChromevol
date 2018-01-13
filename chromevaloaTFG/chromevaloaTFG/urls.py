from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url('', include('chromevaloaAPP.urls')),
    url(r'^browse/search/', include('chromevaloaAPP.urls')),
    url(r'^browse/getBrowseCSV/', include('chromevaloaAPP.urls')),
    url(r'^expressions/search/', include('chromevaloaAPP.urls')),
    url(r'^expressions/getExpressionCSV/', include('chromevaloaAPP.urls')),
    url(r'^browse/', include('chromevaloaAPP.urls')),
    url(r'^blast/programHelp', include('chromevaloaAPP.urls')),
    url(r'^blast/', include('chromevaloaAPP.urls')),
    url(r'^blast/dbHelp', include('chromevaloaAPP.urls')),
    url(r'^unigenes/', include('chromevaloaAPP.urls')),
    url(r'^expressions/', include('chromevaloaAPP.urls')),
    url(r'^details/(?P<accession>\w+)', include('chromevaloaAPP.urls')),
    url(r'^details/jalview/getAlnFile', include('chromevaloaAPP.urls')),
    url(r'^details/jalview/(?P<contig>\w+)', include('chromevaloaAPP.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)

handler404 = 'chromevaloaAPP.views.handler404'
handler500 = 'chromevaloaAPP.views.handler500'

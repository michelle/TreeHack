from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *
from django.views.generic.create_update import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r"^$", direct_to_template, {'template': 'index.html'} ),
                       (r'transferCode/$', GiveGetCode),
                       (r'(?P<my_arg>\d+)/$', direct_to_template,
                        {'template': 'results.html'}, 'results'),


                       )

'''
                       (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       (r'^admin/', include(admin.site.urls)),
                       (r'about/$', direct_to_template,
                        {'template': 'about.html'}, 'about'),

                       (r"^assets/(?P<path>.*)$", 'django.views.static.serve',
                        {'document_root': settings.STATIC_DOC_ROOT}), )
'''
if settings.DEBUG:
    urlpatterns += patterns((r"^assets/(?P<path>.*)$", 'django.views.static.serve',
                             {'document_root': settings.STATIC_DOC_ROOT}),
                            )

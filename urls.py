from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from pizza.entrega.views import listar_pizzas

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^pizza/', include('pizza.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    
    (r'^$', direct_to_template, {'template': 'index.html'}),

    (r'^preparo$', listar_pizzas),

)

from django.conf import settings

if settings.DEBUG:
    import os
    urlpatterns += patterns('',
        (r'^static/(.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(settings.PROJECT_PATH, 'static')}),
    )

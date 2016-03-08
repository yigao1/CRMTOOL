"""
Definition of urls for CRMTALK.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm

# Uncomment the next lines to enable the admin:
from django.views.generic import CreateView
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()
import app.views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url('^register/', app.views.register, name='register'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^details/(?P<leadcompany>.+)$', app.views.details,name='details'),
    url(r'^details/$', app.views.details,name='details'),

    url(r'^leads/', app.views.leads,name='leads'),


)

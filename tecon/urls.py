from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from frontend.views import TextFileView, Http500View
from haystack.views import basic_search
from tecon_app.sitemaps import sitemaps_dict

admin.autodiscover()


urlpatterns = patterns('',
    # Django admin
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^tecon/api/', include('tecon_app.api.urls', namespace='tecon_api')),
    url(r'^tecon/', include('tecon_app.urls', namespace='tecon')),
    url(
        r'^profile/$',
        TemplateView.as_view(template_name='tecon/profile.html'),
        name="profile"),
    url(r'^search/$', basic_search, name='search'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': settings.LOGOUT_REDIRECT_URL},
        name="account_logout"),
    (r'^accounts/', include('allauth.urls')),

    # Test pages
    url(r'^500test/$', view=Http500View.as_view()),
    url(r'^403/$', 'django.views.defaults.permission_denied'),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^500/$', 'django.views.defaults.server_error'),

    # SEO API's
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps_dict}),
    url(r'^robots.txt$', TextFileView.as_view(content_type='text/plain', template_name='robots.txt')),

)

# https://github.com/mbi/django-rosetta
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )

if settings.DEBUG:
    urlpatterns.insert(0,
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )
    urlpatterns.insert(0,
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True})
    )

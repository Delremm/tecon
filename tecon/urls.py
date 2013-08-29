from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
from frontend.views import TextFileView, Http500View

admin.autodiscover()

sitemaps = {
    # Place sitemaps here
}

urlpatterns = patterns('',
    # Django admin
    url(r'^admin/', include(admin.site.urls)),

    url(r'^tecon/api/', include('tecon_app.api.urls', namespace='tecon_api')),
    url(r'^tecon/', include('tecon_app.urls', namespace='tecon')),

    # Test pages
    url(r'^500test/$', view=Http500View.as_view()),
    url(r'^403/$', 'django.views.defaults.permission_denied'),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^500/$', 'django.views.defaults.server_error'),

    # SEO API's
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^robots.txt$', TextFileView.as_view(content_type='text/plain', template_name='robots.txt')),

    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns.insert(0,
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )
    urlpatterns.insert(0,
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True})
    )

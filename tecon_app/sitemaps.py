# coding: utf-8

from django.contrib.sitemaps import Sitemap, FlatPageSitemap
from django.core.urlresolvers import reverse
from tecon_app.models import Trial


class TrialSitemap(Sitemap):
    changefreq = "dayly"
    priority = 0.5

    def items(self):
        return Trial.objects.filter()

    def lastmod(self, obj):
        return obj.created


class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return ['index', 'tecon:main', 'tecon:create_test', 'tecon:tests']

    def location(self, item):
        return reverse(item)


sitemaps_dict = {
    'static': StaticViewSitemap,
    'trials': TrialSitemap,
    'flatpages': FlatPageSitemap
}

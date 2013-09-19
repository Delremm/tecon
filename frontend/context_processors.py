from django.contrib.sites.models import get_current_site
from django.utils.functional import SimpleLazyObject
from django.conf import settings

def site(request):
    return {
        'site': SimpleLazyObject(lambda: get_current_site(request)),
        'site_name': settings.SITE_VERBOSE_NAME,
        'site_tagline': settings.SITE_TAGLINE,
        'use_less': getattr(settings, 'USE_LESS', False),
        'config': settings.SITE_CONFIG,
        'common_keywords': settings.COMMON_KEYWORDS
    }

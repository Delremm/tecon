# coding: utf-8

"""
Project specific settings
"""
from .defaults import *

# Admins receive 500 errors, managers receive 404 errors.
ADMINS = (
    ('tecon', 'fhpt@yandex.ru'),
)
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'admin@tec0.ru'
EMAIL_SUBJECT_PREFIX = '[Django][tecon] '

# Database to use
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     'tecon',
        'USER':     'tecon',
        'PASSWORD': 'tecon1',
        'OPTIONS':  {'autocommit': True,},   # Stop that "current transaction is aborted" error
    },
}

SECRET_KEY = '+3d$)xhp6za+%8&=#*l&e#u!hz-9q)dv9_jjg%s=r4z5g!3xi#'


MEDIA_ROOT = os.path.abspath(os.path.join(ROOT_DIR, '..', 'tecon_media'))
STATIC_ROOT = os.path.abspath(os.path.join(ROOT_DIR, '..', 'tecon_static'))


# Apps to use
INSTALLED_APPS += (
    # Site parts
    'frontend',
    'tecon_app',

    # Support libs
    'haystack',
    'google_analytics',
    'crispy_forms',
    'vk_iframe',
    'rest_framework',
    "categories",
    "categories.editor",
    #allauth for sign up
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'filer',
    'mptt',
    'easy_thumbnails',
#    https://github.com/mbi/django-rosetta
    'rosetta',

    'django.contrib.flatpages',
    'django.contrib.admin',
)


TEMPLATE_CONTEXT_PROCESSORS += (
    'frontend.context_processors.site',
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

# Consistent date formatting
FORMAT_MODULE_PATH = 'tecon.settings.locale'  

# App specific settings


#site name used in <title>
SITE_VERBOSE_NAME = u'Конструктор тестов'
SITE_TAGLINE = u'просто создавайте тесты, это здорово.'
SITE_CONFIG = {
    'tests_sorting': [
        {
            'title': 'по дате ^',
            'name': 'created'
        },
        {
            'title': 'по дате v',
            'name': '-created'
        }
    ]
}




USE_LESS = False


THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


# Vkontakte-iframe
VK_APP_ID = '3841148'                   # Application ID
VK_APP_KEY = u'Конструктор тестов'               # Application key
VK_APP_SECRET = 'BQpx965F5cG24dgAQ9dj'  # Secure key

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'vk_iframe.backends.VkontakteUserBackend',
    "allauth.account.auth_backends.AuthenticationBackend",
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #vk
    'vk_iframe.middleware.IFrameFixMiddleware',
    'vk_iframe.middleware.AuthenticationMiddleware',

    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'vk_iframe.middleware.LoginRequiredMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

# 'vk_iframe.middleware.LoginRequiredMiddleware' anauthenticated urls
PUBLIC_URLS = [
    '^admin/$',
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(ROOT_DIR, 'whoosh_index'),
    },
}

# https://github.com/mbi/django-rosetta

YANDEX_TRANSLATE_KEY = 'trnsl.1.1.20130911T031328Z.d74fa7ff2d9e00bb.ee68816b4518527186d261a097ff4482ea058504'

from allauth_settings import *
LOGIN_REDIRECT_URL = '/tecon/'
LOGOUT_REDIRECT_URL = '/tecon/'

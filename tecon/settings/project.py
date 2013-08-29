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

DEFAULT_FROM_EMAIL = 'sysadmin@default.com'
EMAIL_SUBJECT_PREFIX = '[Django][tecon] '

# Database to use
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     'tecon',
        'USER':     'tecon',
        'PASSWORD': '',
        'OPTIONS':  {'autocommit': True,},   # Stop that "current transaction is aborted" error
    },
}

SECRET_KEY = '+3d$)xhp6za+%8&=#*l&e#u!hz-9q)dv9_jjg%s=r4z5g!3xi#'

# Apps to use
INSTALLED_APPS += (
    # Site parts
    'frontend',
    'tecon_app',

    # Support libs
    'google_analytics',
    'crispy_forms',
    'vk_iframe',
    'rest_framework',
    #django-cms
    'menus',
    'sekizai',
    'filer',
    'mptt',
    'easy_thumbnails',
    'cms',
    'cms.plugins.text',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    'django.contrib.admin',
)

MIDDLEWARE_CLASSES += (
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'frontend.context_processors.site',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

# Consistent date formatting
FORMAT_MODULE_PATH = 'tecon.settings.locale'  

# App specific settings


#site name used in <title>
SITE_VERBOSE_NAME = u'Конструктор тестов'
SITE_TAGLINE = u'создавайте тесты и отправляйте друзьям.'

USE_LESS = False

#django-cms
CMS_TEMPLATES = (
    ('cms_template.html', 'Default cms_template'),
)

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
    'vk_iframe.middleware.LoginRequiredMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
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

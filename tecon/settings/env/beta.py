from .. import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = True

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     'tecon',
        'USER':     'tecon',
        'PASSWORD': '',
    },
}

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
)

ALLOWED_HOSTS = (
    'tec0.ru',
    'www.tec0.ru'
)

CACHES['default']['KEY_PREFIX'] = '.beta'

#INSTALLED_APPS += ('gunicorn',)

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
    'tecon.testing.mycompany.tld',
)

CACHES['default']['KEY_PREFIX'] = '.beta'

#INSTALLED_APPS += ('gunicorn',)

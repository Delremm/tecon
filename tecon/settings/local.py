# coding: utf-8

"""
Local settings for development.
"""
from .project import INSTALLED_APPS, MIDDLEWARE_CLASSES

# Output to console
import logging, sys, os
#logging.basicConfig(level=logging.DEBUG, stream=sys.stderr)

# Database to use
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.sqlite3',
        'NAME':     'db.sqlite3',
        'USER':     '',
        'PASSWORD': '',
    },
}

SRC_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
ROOT_DIR = SRC_DIR  # os.path.dirname(SRC_DIR)
MEDIA_ROOT   = ROOT_DIR + '/web/media'
STATIC_ROOT = ROOT_DIR + '/web/static'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Debugging assistance

WSGI_APPLICATION = 'tecon.wsgi.development.application'

INSTALLED_APPS += (
    'debug_toolbar',
    #'django_extensions',
    'debugtools',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'debugtools.middleware.XViewMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.cache.CacheDebugPanel',
    #'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

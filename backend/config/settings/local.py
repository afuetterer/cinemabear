# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import,unused-wildcard-import,used-before-assignment

""" Local developlment and testing Django settings"""

from .base import *

SECRET_KEY = ENVIRONMENT(
    "DJANGO_SECRET_KEY", default=",3>h[+-x>'LXwfnaUxwDHvUT@dnA@'+Nvs7rdU;Z4Ezq4M=mHy"
)
DEBUG = ENVIRONMENT.bool("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ("debug_toolbar",)  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if ENVIRONMENT("USE_DOCKER") == "yes":
    import socket

    HOSTNAME, _, IPS = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "1" for ip in IPS]

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ("django_extensions",)

# -*- coding: utf-8 -*-
# pylint: disable=invalid-name

""" WSGI application for cinemabear project """

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)

# -*- coding: utf-8 -*-
""" URLconf for cinemabear project """

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "cinemabear administration"
admin.site.site_title = "cinemabear administration"
admin.site.index_title = "Welcome to cinemabear administration"

urlpatterns = [
    path("admin/", admin.site.urls),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

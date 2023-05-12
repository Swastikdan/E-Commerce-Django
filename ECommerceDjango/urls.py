# This code is defining the URL patterns for a Django web application.
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('webstore.urls')),
]

if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


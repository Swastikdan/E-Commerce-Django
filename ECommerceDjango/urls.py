# This code is defining the URL patterns for a Django web application.
from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('webstore.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

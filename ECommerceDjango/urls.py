from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('webstore.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'webstore.views.home.handle_404'
handler500 = 'webstore.views.home.handle_500'
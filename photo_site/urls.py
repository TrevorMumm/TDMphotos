from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gallery.admin import custom_admin_site

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    #path('admin/', admin.site.urls),
    #path('adminsortable2/', include('adminsortable2.urls')),
    path('', include('gallery.urls')),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

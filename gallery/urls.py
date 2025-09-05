# gallery/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .admin import custom_admin_site

app_name = "gallery"

urlpatterns = [
    path("", views.WelcomeView.as_view(), name="welcome"),

    # Custom admin site (includes its own /upload/ via CustomAdminSite.get_urls)
    path("admin/", custom_admin_site.urls),

    # Folder hierarchy
    path("folders/", views.FolderListView.as_view(), name="folder_list"),
    path("folders/<slug:slug>/", views.FolderDetailView.as_view(), name="folder_detail"),

    # Albums and photos
    path("albums/", views.AlbumListView.as_view(), name="album_list"),
    path("albums/<int:pk>/", views.AlbumDetailView.as_view(), name="album_detail"),
    path("upload/", views.PhotoUploadView.as_view(), name="upload_photo"),
    path("all_photos/", views.AllPhotosView.as_view(), name="all_photos"),
    path("view_selected_photos/", views.ViewSelectedPhotosView.as_view(), name="view_selected_photos"),

    # Contact
    path("contact/", views.contact, name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#OLD WORKING
# from django.conf import settings
# from django.conf.urls.static import static
# from django.urls import path
# from . import views
# from .views import WelcomeView, AlbumListView, AlbumDetailView, PhotoUploadView, MultiPhotoUploadView, AllPhotosView, ViewSelectedPhotosView
# from .admin import custom_admin_site

# urlpatterns = [
#     path('', WelcomeView.as_view(), name='welcome'),
#     path('admin/', custom_admin_site.urls),
#     path("folders/", views.FolderListView.as_view(), name="folder_list"),
#     path("folders/<slug:slug>/", views.FolderDetailView.as_view(), name="folder_detail"),
#     path('albums/', AlbumListView.as_view(), name='album_list'),
#     path('albums/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
#     path('upload/', PhotoUploadView.as_view(), name='upload_photo'),
#     path('admin/upload/', MultiPhotoUploadView.as_view(), name='multi_photo_upload'),
#     path('all_photos/', AllPhotosView.as_view(), name='all_photos'),
#     path('contact/', views.contact, name='contact'),
#     path('contact/', views.contact, name='contact'),
#     path('view_selected_photos/', ViewSelectedPhotosView.as_view(), name='view_selected_photos'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views
from .views import WelcomeView, AlbumListView, AlbumDetailView, PhotoUploadView, AllPhotosView

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('albums/', AlbumListView.as_view(), name='album_list'),
    path('albums/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('upload/', PhotoUploadView.as_view(), name='upload_photo'),
    path('all_photos/', AllPhotosView.as_view(), name='all_photos'),
    path('contact/', views.contact, name='contact'),
]

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from .models import Album, Photo
from .forms import PhotoUploadForm
from urllib.parse import urlencode
import logging

logger = logging.getLogger(__name__)

class WelcomeView(View):
    def get(self, request):
        return render(request, 'gallery/welcome.html')

class AlbumListView(View):
    def get(self, request):
        albums = Album.objects.all()
        return render(request, 'gallery/album_list.html', {'albums': albums})

class AlbumDetailView(View):
    def get(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        photos = album.photos.all()
        return render(request, 'gallery/album_detail.html', {'album': album, 'photos': photos})

class PhotoUploadView(View):
    def get(self, request):
        form = PhotoUploadForm()
        return render(request, 'gallery/upload_photo.html', {'form': form})

    def post(self, request):
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_list')
        return render(request, 'gallery/upload_photo.html', {'form': form})

class AllPhotosView(View):
    def get(self, request):
        photos = Photo.objects.all()
        albums = Album.objects.all()
        return render(request, 'gallery/all_photos.html', {'photos': photos, 'albums': albums})

class ViewSelectedPhotosView(View):
    def get(self, request):
        photo_ids = request.GET.get('photo_ids', '')
        logger.debug(f"Received photo IDs: {photo_ids}")
        if photo_ids:
            photo_ids_list = photo_ids.split(',')
            photos = Photo.objects.filter(id__in=photo_ids_list)
            logger.debug(f"Found photos: {photos}")
            return render(request, 'gallery/view_selected_photos.html', {'photos': photos})
        return redirect('all_photos')

def contact(request):
    return render(request, 'gallery/contact.html')

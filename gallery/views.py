from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from .models import Album, Photo
from .forms import PhotoUploadForm
from urllib.parse import urlencode
import logging
from .forms import MultiPhotoUploadForm

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

class MultiPhotoUploadView(View):
    def get(self, request):
        form = MultiPhotoUploadForm()
        return render(request, 'gallery/upload_photo.html', {'form': form})

    def post(self, request):
        form = MultiPhotoUploadForm(request.POST)
        files = request.FILES.getlist('images')  # Manual file grab

        if form.is_valid() and files:
            title = form.cleaned_data['title']
            albums = list(form.cleaned_data['albums'])  # convert queryset to list
            tags = form.cleaned_data['tags']
            new_album_title = form.cleaned_data['new_album_title']

            if new_album_title:
                new_album = Album.objects.create(title=new_album_title)
                albums.append(new_album)

            for f in files:
                photo = Photo.objects.create(title=title, image=f)
                photo.albums.set(albums)
                photo.tags.set(tags)

            return redirect('album_list')

        return render(request, 'gallery/upload_photo.html', {'form': form})

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

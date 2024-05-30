from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Album, Photo
from .forms import PhotoUploadForm

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
        photos = album.photos.all()  # Correct related name
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


def contact(request):
    return render(request, 'gallery/contact.html')

from django.shortcuts import render
from django.views import View
from .models import Album, Photo, WelcomePageSettings

class WelcomeView(View):
    def get(self, request):
        settings = WelcomePageSettings.objects.first()
        albums = Album.objects.all()
        return render(request, 'gallery/welcome.html', {'settings': settings, 'albums': albums})

class AlbumListView(View):
    def get(self, request):
        albums = Album.objects.all()
        return render(request, 'gallery/album_list.html', {'albums': albums})

class AlbumDetailView(View):
    def get(self, request, pk):
        album = Album.objects.get(pk=pk)
        albums = Album.objects.all()
        return render(request, 'gallery/album_detail.html', {'album': album, 'albums': albums})

class PhotoUploadView(View):
    def get(self, request):
        form = PhotoForm()
        albums = Album.objects.all()
        return render(request, 'gallery/upload_photo.html', {'form': form, 'albums': albums})

    def post(self, request):
        form = PhotoForm(request.POST, request.FILES)
        albums = Album.objects.all()
        if form.is_valid():
            form.save()
            return redirect('album_list')
        return render(request, 'gallery/upload_photo.html', {'form': form, 'albums': albums})

class AllPhotosView(View):
    def get(self, request):
        photos = Photo.objects.all()
        albums = Album.objects.all()
        return render(request, 'gallery/all_photos.html', {'photos': photos, 'albums': albums})

def contact(request):
    return render(request, 'gallery/contact.html')
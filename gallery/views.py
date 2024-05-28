# views.py

from django.shortcuts import render
from django.views import View
from .models import Album, Photo, WelcomePageSettings
from django.conf import settings

class WelcomeView(View):
    def get(self, request):
        context = {
            'background_image_url': 'https://s3.us-south.cloud-object-storage.appdomain.cloud/photographysite/media/welcome_backgrounds/Northern_Lights_Eau_Claire_WI-4.jpg',
            'background_image_2_url': 'https://s3.us-south.cloud-object-storage.appdomain.cloud/photographysite/media/welcome_backgrounds/Black_Crowned_NightHeron_w__Fish_FINAL.png',
            'background_image_3_url': 'https://s3.us-south.cloud-object-storage.appdomain.cloud/photographysite/media/welcome_backgrounds/GOAT_UltraSharpMacroBubble-8_FINAL.jpg',
            'background_image_4_url': 'https://s3.us-south.cloud-object-storage.appdomain.cloud/photographysite/media/welcome_backgrounds/Tan_Bison_Irvine_Park_FINAL.png'
        }
        albums = Album.objects.all()
        return render(request, 'gallery/welcome.html', {'settings': context, 'albums': albums})


    # def get(self, request):
    #     settings = WelcomePageSettings.objects.first()
    #     albums = Album.objects.all()
    #     return render(request, 'gallery/welcome.html', {'settings': settings, 'albums': albums})
    
    def __str__(self):
        return self.title

    @property
    def url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return ''

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

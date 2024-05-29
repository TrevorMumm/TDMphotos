from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from .models import Photo, Album, Tag, WelcomePageSettings
from .forms import MultiplePhotoUploadForm

class AlbumAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'order', 'created_at']
    fields = ['title', 'description', 'cover_image']

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'uploaded_at']
    search_fields = ['title']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('multiple-upload/', self.admin_site.admin_view(self.multiple_upload_view), name='multiple-upload')
        ]
        return custom_urls + urls

    def multiple_upload_view(self, request):
        if request.method == 'POST':
            form = MultiplePhotoUploadForm(request.POST, request.FILES)
            if form.is_valid():
                albums = form.cleaned_data['albums']
                tags = form.cleaned_data['tags']
                for image in request.FILES.getlist('images'):
                    photo = Photo(image=image)
                    photo.save()
                    photo.albums.set(albums)
                    photo.tags.set(tags)
                self.message_user(request, "Photos uploaded successfully.")
                return redirect('admin:gallery_photo_changelist')
        else:
            form = MultiplePhotoUploadForm()
        context = {
            **self.admin_site.each_context(request),
            'form': form,
            'title': 'Multiple Photo Upload',
        }
        return render(request, 'admin/multiple_photo_upload.html', context)

class WelcomePageSettingsAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    fields = ['background_image', 'background_image_2', 'background_image_3', 'background_image_4']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag)
admin.site.register(WelcomePageSettings, WelcomePageSettingsAdmin)
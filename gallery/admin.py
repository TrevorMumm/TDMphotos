from django.contrib import admin
from django.urls import path
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from .models import Photo, Album, Tag, WelcomePageSettings
from .forms import PhotoUploadForm
from .views import MultiPhotoUploadView
from django.contrib.admin.views.decorators import staff_member_required

# Wrap your custom view
multi_upload_view = staff_member_required(MultiPhotoUploadView.as_view())

# Define custom AdminSite
class CustomAdminSite(admin.AdminSite):
    site_header = "TDM Photography Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload/', multi_upload_view, name='multi_photo_upload'),
        ]
        return custom_urls + urls

# Instantiate custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')

# Admin classes
class AlbumAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'order', 'created_at']
    fields = ['title', 'description', 'cover_image']

class PhotoAdmin(admin.ModelAdmin):
    form = PhotoUploadForm
    list_display = ['__str__', 'uploaded_at']
    search_fields = ['title']
    change_list_template = "gallery/photo/change_list.html"

class WelcomePageSettingsAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title', 'background_image', 'background_image_2', 'background_image_3', 'background_image_4']

# Register models with custom admin
custom_admin_site.register(Photo, PhotoAdmin)
custom_admin_site.register(Album, AlbumAdmin)
custom_admin_site.register(Tag)
custom_admin_site.register(WelcomePageSettings, WelcomePageSettingsAdmin)


#OLD WORKING
# from django.contrib import admin
# from django.urls import path
# from django.shortcuts import render, redirect
# from django.utils.html import format_html
# from adminsortable2.admin import SortableAdminMixin
# from .models import Photo, Album, Tag, WelcomePageSettings
# from .forms import PhotoUploadForm

# class AlbumAdmin(SortableAdminMixin, admin.ModelAdmin):
#     list_display = ['title', 'order', 'created_at']
#     fields = ['title', 'description', 'cover_image']

# class PhotoAdmin(admin.ModelAdmin):
#     form = PhotoUploadForm
#     list_display = ['__str__', 'uploaded_at']
#     search_fields = ['title']

# class WelcomePageSettingsAdmin(admin.ModelAdmin):
#     list_display = ['title']
#     fields = ['title', 'background_image', 'background_image_2', 'background_image_3', 'background_image_4']

# admin.site.register(Photo, PhotoAdmin)
# admin.site.register(Album, AlbumAdmin)
# admin.site.register(Tag)
# admin.site.register(WelcomePageSettings, WelcomePageSettingsAdmin)
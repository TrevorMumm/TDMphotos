from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from .models import Photo, Album, Tag, WelcomePageSettings
from .forms import PhotoUploadForm

class AlbumAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'order', 'created_at']
    fields = ['title', 'description', 'cover_image']

class PhotoAdmin(admin.ModelAdmin):
    form = PhotoUploadForm
    list_display = ['__str__', 'uploaded_at']
    search_fields = ['title']

class WelcomePageSettingsAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title', 'background_image', 'background_image_2', 'background_image_3', 'background_image_4']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag)
admin.site.register(WelcomePageSettings, WelcomePageSettingsAdmin)
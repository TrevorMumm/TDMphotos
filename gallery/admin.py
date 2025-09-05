# gallery/admin.py

from django.contrib import admin, messages
from django.urls import path
from adminsortable2.admin import SortableAdminMixin
from django.contrib.admin.views.decorators import staff_member_required

from .models import Folder, Photo, Album, Tag, WelcomePageSettings
from .forms import PhotoUploadForm
from .views import MultiPhotoUploadView
from django import forms
from django.db.models import Count
from django.utils.html import format_html

# Wrap your custom view
multi_upload_view = staff_member_required(MultiPhotoUploadView.as_view())

#define album admin action form
class AlbumActionForm(forms.Form):
    # required by Django admin; choices are populated at runtime
    action = forms.ChoiceField(required=False)
    # required hidden field used by admin for “select all across pages”
    select_across = forms.BooleanField(required=False, initial=0, widget=forms.HiddenInput)

    # your extra control
    folder = forms.ModelChoiceField(
        queryset=Folder.objects.all(),
        required=False,
        label="Move to folder"
    )

# Define custom AdminSite
class CustomAdminSite(admin.AdminSite):
    site_header = "TDM Photography Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload/', multi_upload_view, name='multi_photo_upload'),
        ]
        return custom_urls + urls

# ADD this inline above FolderAdmin
class AlbumInline(admin.TabularInline):
    model = Album
    fields = ("title", "order", "created_at")
    readonly_fields = ("order", "created_at")
    extra = 0
    show_change_link = True
    ordering = ("order", "title")

# Instantiate custom admin site
custom_admin_site = CustomAdminSite(name='custom_admin')

# ----- Default admin site registrations -----

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ("thumb", "name", "order", "created_at", "album_count", "albums_list")
    list_display_links = ("thumb", "name")
    list_editable = ("order",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    fields = ("name", "slug", "description", "cover_image", "order")
    inlines = [AlbumInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_album_count=Count("albums"))

    def album_count(self, obj):
        return obj._album_count
    album_count.short_description = "Albums"
    album_count.admin_order_field = "_album_count"

    def albums_list(self, obj):
        titles = list(obj.albums.order_by("order", "title").values_list("title", flat=True)[:10])
        more = obj.albums.count() - len(titles)
        out = ", ".join(titles)
        if more > 0:
            out += f" … (+{more})"
        return out
    albums_list.short_description = "Album titles"

    def thumb(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="height:40px;width:60px;object-fit:cover;border-radius:4px;" />', obj.cover_image.url)
        return "—"
    thumb.short_description = "Cover"

@admin.register(Album)
class AlbumAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ("folder", "title", "description", "cover_image")
    list_display = ("title", "folder", "order", "created_at")
    list_display_links = ("title",)
    list_editable = ("folder",)
    list_filter = ("folder",)
    search_fields = ("title", "description")
    autocomplete_fields = ("folder",)

    # IMPORTANT: keep only the real sortable field here
    ordering = ("order", "title")

    # optionally pin this explicitly (some versions respect this)
    default_order_field = "order"

    action_form = AlbumActionForm
    actions = ("move_to_folder", "clear_folder")

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    form = PhotoUploadForm
    list_display = ("id", "title", "albums_display", "uploaded_at")
    list_filter = ("albums", "tags")
    search_fields = ("title",)
    filter_horizontal = ("albums", "tags")

    def albums_display(self, obj):
        return ", ".join(a.title for a in obj.albums.all())
    albums_display.short_description = "Albums"

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(WelcomePageSettings)
class WelcomePageSettingsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("title", "background_image", "background_image_2", "background_image_3", "background_image_4")

# ----- Custom admin site registrations -----

custom_admin_site.register(Folder, FolderAdmin)
custom_admin_site.register(Album, AlbumAdmin)
custom_admin_site.register(Photo, PhotoAdmin)
custom_admin_site.register(Tag, TagAdmin)
custom_admin_site.register(WelcomePageSettings, WelcomePageSettingsAdmin)


# #OLD WORKING
# from django.contrib import admin
# from django.urls import path
# from django.utils.html import format_html
# from adminsortable2.admin import SortableAdminMixin
# from .models import Folder, Photo, Album, Tag, WelcomePageSettings
# from .forms import PhotoUploadForm
# from .views import MultiPhotoUploadView
# from django.contrib.admin.views.decorators import staff_member_required

# # Wrap your custom view
# multi_upload_view = staff_member_required(MultiPhotoUploadView.as_view())

# # Define custom AdminSite
# class CustomAdminSite(admin.AdminSite):
#     site_header = "TDM Photography Admin"

#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path('upload/', multi_upload_view, name='multi_photo_upload'),
#         ]
#         return custom_urls + urls

# # Instantiate custom admin site
# custom_admin_site = CustomAdminSite(name='custom_admin')

# # Admin classes
# class AlbumAdmin(SortableAdminMixin, admin.ModelAdmin):
#     list_display = ['title', 'order', 'created_at']
#     fields = ['title', 'description', 'cover_image']

# class PhotoAdmin(admin.ModelAdmin):
#     form = PhotoUploadForm
#     list_display = ['__str__', 'uploaded_at']
#     search_fields = ['title']
#     change_list_template = "gallery/photo/change_list.html"

# class WelcomePageSettingsAdmin(admin.ModelAdmin):
#     list_display = ['title']
#     fields = ['title', 'background_image', 'background_image_2', 'background_image_3', 'background_image_4']

# # Register models with custom admin
# custom_admin_site.register(Photo, PhotoAdmin)
# custom_admin_site.register(Album, AlbumAdmin)
# custom_admin_site.register(Tag)
# custom_admin_site.register(WelcomePageSettings, WelcomePageSettingsAdmin)

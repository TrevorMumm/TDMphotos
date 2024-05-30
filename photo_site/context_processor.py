# photo_site/context_processors.py

from django.conf import settings
from gallery.models import Album, WelcomePageSettings  # Ensure Album is imported

def all_albums(request):
    return {
        'all_albums': Album.objects.all()
    }

def custom_settings(request):
    welcome_settings = WelcomePageSettings.objects.first()
    return {
        'settings': {
            'title': welcome_settings.title if welcome_settings else '',
            'background_image_url': welcome_settings.background_image.url if welcome_settings and welcome_settings.background_image else '',
            'background_image_2_url': welcome_settings.background_image_2.url if welcome_settings and welcome_settings.background_image_2 else '',
            'background_image_3_url': welcome_settings.background_image_3.url if welcome_settings and welcome_settings.background_image_3 else '',
            'background_image_4_url': welcome_settings.background_image_4.url if welcome_settings and welcome_settings.background_image_4 else '',
        }
    }

# photo_site/context_processors.py

from django.conf import settings

def custom_settings(request):
    # print("BACKGROUND_IMAGE_URL:", settings.BACKGROUND_IMAGE_URL)
    # print("BACKGROUND_IMAGE_2_URL:", settings.BACKGROUND_IMAGE_2_URL)
    # print("BACKGROUND_IMAGE_3_URL:", settings.BACKGROUND_IMAGE_3_URL)
    # print("BACKGROUND_IMAGE_4_URL:", settings.BACKGROUND_IMAGE_4_URL)
    return {
        'settings': {
            'background_image_url': settings.BACKGROUND_IMAGE_URL,
            'background_image_2_url': settings.BACKGROUND_IMAGE_2_URL,
            'background_image_3_url': settings.BACKGROUND_IMAGE_3_URL,
            'background_image_4_url': settings.BACKGROUND_IMAGE_4_URL,
        }
    }

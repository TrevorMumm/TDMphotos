from .models import Folder
from django.db.models import Prefetch
from .models import Album

def nav_folders(request):
    return {
        "NAV_FOLDERS": Folder.objects.order_by("order", "name").prefetch_related(
            Prefetch("albums", queryset=Album.objects.order_by("order", "title"))
        )
    }

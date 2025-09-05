# gallery/management/commands/ensure_folders.py

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from gallery.models import Folder, Album

class Command(BaseCommand):
    help = "Ensure all albums are assigned to a folder; create 'Unsorted' if necessary."

    def handle(self, *args, **options):
        default, _ = Folder.objects.get_or_create(
            name="Unsorted",
            defaults={"slug": slugify("Unsorted"), "description": "Default folder for existing albums", "order": 0},
        )
        missing = Album.objects.filter(folder__isnull=True)
        count = missing.update(folder=default)
        self.stdout.write(self.style.SUCCESS(f"Assigned {count} album(s) to '{default.name}'."))

# gallery/migrations/0005_folder_hierarchy.py

from django.db import migrations, models
import django.db.models.deletion
from django.utils.text import slugify

def create_default_folder_and_assign(apps, schema_editor):
    Folder = apps.get_model("gallery", "Folder")
    Album = apps.get_model("gallery", "Album")
    default, _ = Folder.objects.get_or_create(
        name="Unsorted",
        defaults={
            "slug": slugify("Unsorted"),
            "description": "Default folder for existing albums",
            "order": 0,
        },
    )
    for album in Album.objects.all():
        if getattr(album, "folder_id", None) is None:
            album.folder_id = default.id
            album.save(update_fields=["folder"])

class Migration(migrations.Migration):

    # CHANGE THIS to your latest applied migration in 'gallery'
    dependencies = [
        ("gallery", "0004_remove_photo_name_remove_photo_url_delete_sharedlink"),
    ]

    operations = [
        migrations.CreateModel(
            name="Folder",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField(blank=True, max_length=255, unique=True)),
                ("description", models.TextField(blank=True)),
                ("order", models.PositiveIntegerField(db_index=True, default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ("order", "name")},
        ),
        migrations.AddField(
            model_name="album",
            name="folder",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="albums",
                to="gallery.folder",
                help_text="Top-level folder containing this album, e.g., 'Style'.",
            ),
        ),
        migrations.AddConstraint(
            model_name="album",
            constraint=models.UniqueConstraint(
                fields=("folder", "title"),
                name="uq_album_folder_title",
            ),
        ),
        migrations.RunPython(
            create_default_folder_and_assign,
            reverse_code=migrations.RunPython.noop,
        ),
    ]

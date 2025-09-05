from django.db import models
from django.utils.text import slugify
from django.urls import reverse

def get_absolute_url(self):
    return reverse("gallery:album_detail", args=[self.pk])

class Folder(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    cover_image = models.ImageField(upload_to="media/folder_covers/", blank=True, null=True)

    class Meta:
        ordering = ("order", "name")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    @property
    def cover_url(self):
        if self.cover_image and hasattr(self.cover_image, "url"):
            return self.cover_image.url
        return ""

class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Album(models.Model):
    folder = models.ForeignKey(
        "Folder",
        on_delete=models.PROTECT,
        related_name="albums",
        null=True,
        blank=True,
        help_text="Top-level folder containing this album, e.g., 'Style'.",
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='media/album_covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']
        constraints = [
            models.UniqueConstraint(
                fields=["folder", "title"],
                name="uq_album_folder_title"
            )
        ]

    def __str__(self):
        if getattr(self, "folder_id", None):
            return f"{self.folder.name} → {self.title}"
        return self.title
    
    @property
    def cover_url(self):
        if self.cover_image and hasattr(self.cover_image, 'url'):
            return self.cover_image.url
        return ''

class Photo(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='media/photos/')
    albums = models.ManyToManyField(Album, related_name='photos')
    tags = models.ManyToManyField(Tag, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title or str(self.image)

    def url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return ''

class WelcomePageSettings(models.Model):
    title = models.CharField(max_length=100, default="Welcome to TDM Photography")
    background_image = models.ImageField(upload_to='media/welcome/', blank=True, null=True)
    background_image_2 = models.ImageField(upload_to='media/welcome/', blank=True, null=True)
    background_image_3 = models.ImageField(upload_to='media/welcome/', blank=True, null=True)
    background_image_4 = models.ImageField(upload_to='media/welcome/', blank=True, null=True)

    def __str__(self):
        return self.title

# models.py

from django.db import models
from adminsortable2.admin import SortableAdminMixin

class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='media/album_covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
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
    background_image = models.ImageField(upload_to='media/welcome_backgrounds/', blank=True, null=True)
    background_image_2 = models.ImageField(upload_to='media/welcome_backgrounds/', blank=True, null=True)
    background_image_3 = models.ImageField(upload_to='media/welcome_backgrounds/', blank=True, null=True)
    background_image_4 = models.ImageField(upload_to='media/welcome_backgrounds/', blank=True, null=True)

    def __str__(self):
        return "Welcome Page Settings"

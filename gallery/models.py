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
    cover_image = models.ImageField(upload_to='album_covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='photos/')
    albums = models.ManyToManyField(Album, related_name='photos')
    tags = models.ManyToManyField(Tag, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title or str(self.image)

class WelcomePageSettings(models.Model):
    background_image = models.ImageField(upload_to='welcome_backgrounds/', blank=True, null=True)
    background_image_2 = models.ImageField(upload_to='welcome_backgrounds/', blank=True, null=True)  # New field
    background_image_3 = models.ImageField(upload_to='welcome_backgrounds/', blank=True, null=True)  # New field
    background_image_4 = models.ImageField(upload_to='welcome_backgrounds/', blank=True, null=True)

    def __str__(self):
        return "Welcome Page Settings"
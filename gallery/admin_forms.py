from django import forms
from .models import Album, Photo
from .widgets import MultipleFileInput

class MultiplePhotoAdminUploadForm(forms.ModelForm):
    images = forms.FileField(widget=MultipleFileInput, required=True)
    
    class Meta:
        model = Photo
        fields = ['title', 'images', 'albums', 'tags']
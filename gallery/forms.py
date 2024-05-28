from django import forms
from .models import Album, Tag
from .widgets import MultipleFileInput

class MultiplePhotoUploadForm(forms.Form):
    images = forms.FileField(widget=MultipleFileInput(), required=True)
    albums = forms.ModelMultipleChoiceField(queryset=Album.objects.all(), required=True)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)

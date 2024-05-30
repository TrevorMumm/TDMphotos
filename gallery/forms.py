from django import forms
from .models import Album, Tag
from .models import Photo

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image', 'albums', 'tags']

class AlbumAdminForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'cover_image']

    def clean_order(self):
        order = self.cleaned_data.get('order')
        if not isinstance(order, int):
            raise forms.ValidationError("Order must be an integer.")
        return order